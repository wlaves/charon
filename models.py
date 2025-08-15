from ipaddress import ip_address
import fcntl
import json
import time
from config import state_file, dummy_ip, routes, alias_dir

def valid_ip(ip):
    try:
        ip_address(ip)
        return True
    except Exception:
        return False

def load_state():
    """Load state, keeping all IPs without expiry."""
    if not state_file.exists():
        return {dummy_ip: {"timestamp": 0, "route": None}}
    try:
        with open(state_file, "r") as f:
            data = json.load(f)
    except Exception:
        return {dummy_ip: {"timestamp": 0, "route": None}}
    
    # Ensure dummy IP is always present
    if dummy_ip not in data:
        data[dummy_ip] = {"timestamp": 0, "route": None}
    
    return data

def save_state(state):
    with open(state_file, "w") as f:
        json.dump(state, f)

def sync_route_files(state):
    """Write route files based on current state."""
    # Create route-specific IP sets
    route_ips = {}
    for route_key in routes:
        route_ips[route_key] = set([dummy_ip])  # Always include dummy
    
    # Distribute IPs to their routes
    for ip, data in state.items():
        route = data.get("route")
        if route and route in routes:
            route_ips[route].add(ip)
    
    # Write each route file
    for route_key, route_config in routes.items():
        file_path = alias_dir / route_config["file_name"]
        with open(file_path, "w") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            try:
                for ip in sorted(route_ips[route_key]):
                    f.write(ip + "\n")
            finally:
                fcntl.flock(f, fcntl.LOCK_UN)

def set_ip_route(ip, route):
    """Set the route for an IP address."""
    if not valid_ip(ip):
        return
    
    state = load_state()
    
    if route == "disabled" or route is None:
        # Remove from state if disabling
        if ip != dummy_ip and ip in state:
            del state[ip]
    else:
        # Add/update IP with route
        state[ip] = {"timestamp": time.time(), "route": route}
    
    save_state(state)
    sync_route_files(state)

def add_ip(ip):
    """Legacy function - adds IP with default route."""
    set_ip_route(ip, "uk")

def remove_ip(ip):
    """Legacy function - removes IP from routing."""
    set_ip_route(ip, "disabled")

def client_ip(req):
    """Return the real client IP, preferring headers from nginx."""
    ip = req.headers.get("X-Real-IP") or req.headers.get("X-Forwarded-For") or req.remote_addr
    return ip.split(",")[0].strip()

def clear_all_routes():
    """Clear all IPs from all routes, keeping only dummy IP in each file."""
    state = {dummy_ip: {"timestamp": 0, "route": None}}
    save_state(state)
    
    # Write dummy IP to all route files
    for route_key, route_config in routes.items():
        file_path = alias_dir / route_config["file_name"]
        with open(file_path, "w") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            try:
                f.write(dummy_ip + "\n")
            finally:
                fcntl.flock(f, fcntl.LOCK_UN)
