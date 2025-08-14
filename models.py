from ipaddress import ip_address
import fcntl
import json
import time
from config import STATE_FILE, LIST_FILE, DUMMY_IP, EXPIRY_SECONDS

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

def client_ip(req):
    """Return the real client IP, preferring headers from nginx."""
    ip = req.headers.get("X-Real-IP") or req.headers.get("X-Forwarded-For") or req.remote_addr
    return ip.split(",")[0].strip()
