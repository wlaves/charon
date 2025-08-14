from flask import request, jsonify, send_from_directory
from models import load_state, add_ip, remove_ip, valid_ip, client_ip
from config import ALIAS_DIR, TV_IP, DUMMY_IP

def register_routes(app):
    @app.get("/")
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

    @app.get("/state")
    def state():
        state = load_state()
        me = client_ip(request)
        tv_on = TV_IP in state
        self_on = me in state
        return jsonify({"tv": tv_on, "self": self_on, "list": sorted(state.keys())})

    @app.post("/toggle")
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

    @app.get("/alias/<path:fname>")
    def alias(fname):
        return send_from_directory(ALIAS_DIR, fname, mimetype="text/plain")

    @app.get("/debugip")
    def debugip():
        return {
            "remote_addr": request.remote_addr,
            "X-Real-IP": request.headers.get("X-Real-IP"),
            "X-Forwarded-For": request.headers.get("X-Forwarded-For"),
            "all_headers": dict(request.headers)
        }
