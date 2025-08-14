from ipaddress import ip_address
import fcntl
import json
import time
from config import STATE_FILE, ALIAS_DIR, DUMMY_IP, EXPIRY_SECONDS, ROUTES

def valid_ip(ip):
    try:
        ip_address(ip)
        return True
    except Exception:
        return False

def load_state():
    """Load state and drop expired IPs, but always keep dummy."""
    if not STATE_FILE.exists():
        return {DUMMY_IP: {"route": "uk", "timestamp": 0}}
    try:
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
    except Exception:
        return {DUMMY_IP: {"route": "uk", "timestamp": 0}}
    
    # Convert old format to new format if needed
    now = time.time()
    pruned = {}
    for ip, value in data.items():
        if isinstance(value, (int, float)):  # Old format
            if ip == DUMMY_IP or now - value < EXPIRY_SECONDS:
                pruned[ip] = {"route": "uk", "timestamp": value}
        else:  # New format
            if ip == DUMMY_IP or now - value.get("timestamp", 0) < EXPIRY_SECONDS:
                pruned[ip] = value
    
    if DUMMY_IP not in pruned:
        pruned[DUMMY_IP] = {"route": "uk", "timestamp": 0}
    return pruned

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def sync_alias_files(state):
    """Write alias files for each route from state."""
    # Group IPs by route
    routes_ips = {}
    for ip, data in state.items():
        route = data.get("route")
        if route and route in ROUTES:
            if route not in routes_ips:
                routes_ips[route] = []
            routes_ips[route].append(ip)
    
    # Write each route file
    for route_key, route_config in ROUTES.items():
        file_path = ALIAS_DIR / route_config["file_name"]
        with open(file_path, "w") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            try:
                # Always put dummy IP first
                if route_key in routes_ips and DUMMY_IP in routes_ips[route_key]:
                    f.write(DUMMY_IP + "\n")
                    # Write other IPs sorted
                    other_ips = [ip for ip in routes_ips[route_key] if ip != DUMMY_IP]
                    for ip in sorted(other_ips):
                        f.write(ip + "\n")
                elif route_key in routes_ips:
                    # Write all IPs sorted
                    for ip in sorted(routes_ips[route_key]):
                        f.write(ip + "\n")
            finally:
                fcntl.flock(f, fcntl.LOCK_UN)

def add_ip(ip, route="uk"):
    if not valid_ip(ip):
        return
    state = load_state()
    state[ip] = {"route": route, "timestamp": time.time()}
    save_state(state)
    sync_alias_files(state)

def remove_ip(ip):
    state = load_state()
    if ip != DUMMY_IP and ip in state:
        del state[ip]
    save_state(state)
    sync_alias_files(state)

def set_ip_route(ip, route):
    """Set the route for an IP, or remove if route is disabled."""
    if route == "disabled":
        remove_ip(ip)
        return
    
    if not valid_ip(ip) or route not in ROUTES:
        return
    
    state = load_state()
    if ip in state:
        state[ip]["route"] = route
    else:
        state[ip] = {"route": route, "timestamp": time.time()}
    save_state(state)
    sync_alias_files(state)

def client_ip(req):
    """Return the real client IP, preferring headers from nginx."""
    ip = req.headers.get("X-Real-IP") or req.headers.get("X-Forwarded-For") or req.remote_addr
    return ip.split(",")[0].strip()
