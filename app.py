from flask import Flask, request, jsonify, send_from_directory
from ipaddress import ip_address
from pathlib import Path
import fcntl
import json
import time

APP = Flask(__name__)

# --- Config ---
ALIAS_DIR = Path("/var/www/alias")
ALIAS_DIR.mkdir(parents=True, exist_ok=True)
LIST_FILE = ALIAS_DIR / "brittv_hosts.txt"
STATE_FILE = ALIAS_DIR / "state.json"

TV_IP = "192.168.1.170"       # set your Smart TV's IP
DUMMY_IP = "192.0.2.1"        # reserved IP that never expires
EXPIRY_SECONDS = 6 * 3600     # 6 hours

# --- Helpers ---

def client_ip(req):
    """Return the real client IP, preferring headers from nginx."""
    ip = req.headers.get("X-Real-IP") or req.headers.get("X-Forwarded-For") or req.remote_addr
    return ip.split(",")[0].strip()

def valid_ip(ip):
    try:
        ip_address(ip)
        return True
    except Exception:
        return False

def load_state():
    """Load state and drop expired IPs, but always keep dummy."""
    if not STATE_FILE.exists():
        return {DUMMY_IP: 0}
    try:
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
    except Exception:
        return {DUMMY_IP: 0}
    now = time.time()
    pruned = {}
    for ip, ts in data.items():
        if ip == DUMMY_IP or now - ts < EXPIRY_SECONDS:
            pruned[ip] = ts
    if DUMMY_IP not in pruned:
        pruned[DUMMY_IP] = 0
    return pruned

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def sync_alias_file(state):
    """Write alias file from state."""
    with open(LIST_FILE, "w") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            for ip in sorted(state.keys()):
                f.write(ip + "\n")
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)

def add_ip(ip):
    if not valid_ip(ip):
        return
    state = load_state()
    state[ip] = time.time()
    save_state(state)
    sync_alias_file(state)

def remove_ip(ip):
    state = load_state()
    if ip != DUMMY_IP and ip in state:
        del state[ip]
    save_state(state)
    sync_alias_file(state)

# --- Routes ---

@APP.get("/")
def index():
    return f"""
<!doctype html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>brittv</title></head>
<body style="font-family:system-ui;margin:2rem;max-width:40rem">
<h1>brittv</h1>
<label><input type="checkbox" id="tv"> tv</label>
<br><br>
<label><input type="checkbox" id="self"> self ({client_ip(request)})</label>
<br><br>
<h3>Routed:</h3>
<div id="routed"></div>
<script>
async function getState() {{
  const r = await fetch("/state");
  const s = await r.json();
  const selfIp = "{client_ip(request)}";
  document.getElementById("tv").checked = s.tv;
  document.getElementById("self").checked = s.self;
  const routedDiv = document.getElementById("routed");
  routedDiv.innerHTML = "";
  s.list.forEach(ip => {{
    if (ip === "{DUMMY_IP}" || ip === "{TV_IP}" || ip === selfIp) return; // hide dummy, tv, self
    const label = document.createElement("label");
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = true;
    checkbox.addEventListener("change", e => setToggle(ip, e.target.checked));
    label.appendChild(checkbox);
    label.appendChild(document.createTextNode(" " + ip));
    routedDiv.appendChild(label);
    routedDiv.appendChild(document.createElement("br"));
  }});
}}
async function setToggle(name, on) {{
  await fetch("/toggle", {{
    method: "POST",
    headers: {{ "Content-Type": "application/json" }},
    body: JSON.stringify({{ name, on }})
  }});
  await getState();
}}
document.getElementById("tv").addEventListener("change", e => setToggle("tv", e.target.checked));
document.getElementById("self").addEventListener("change", e => setToggle("self", e.target.checked));
getState();
</script>
</body>
</html>
"""

@APP.get("/state")
def state():
    state = load_state()
    me = client_ip(request)
    tv_on = TV_IP in state
    self_on = me in state
    return jsonify({"tv": tv_on, "self": self_on, "list": sorted(state.keys())})

@APP.post("/toggle")
def toggle():
    data = request.get_json(force=True)
    name = data.get("name")
    on = bool(data.get("on"))

    if name == "tv":
        if on:
            add_ip(TV_IP)
        else:
            remove_ip(TV_IP)
    elif name == "self":
        me = client_ip(request)
        if not valid_ip(me):
            return ("bad ip", 400)
        if on:
            add_ip(me)
        else:
            remove_ip(me)
    elif valid_ip(name):
        if on:
            add_ip(name)
        else:
            remove_ip(name)
    else:
        return ("bad toggle", 400)
    return ("ok", 200)

@APP.get("/alias/<path:fname>")
def alias(fname):
    return send_from_directory(ALIAS_DIR, fname, mimetype="text/plain")

@APP.get("/debugip")
def debugip():
    return {
        "remote_addr": request.remote_addr,
        "X-Real-IP": request.headers.get("X-Real-IP"),
        "X-Forwarded-For": request.headers.get("X-Forwarded-For"),
        "all_headers": dict(request.headers)
    }

if __name__ == "__main__":
    APP.run(host="127.0.0.1", port=5000)
