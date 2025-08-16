from pathlib import Path
from common import available_routes, dummy_ip

# Directory and file paths
alias_dir = Path("/var/www/alias")
alias_dir.mkdir(parents=True, exist_ok=True)
state_file = alias_dir / "state.json"

# Network configuration - customize these for your setup
tv_ip = {"TV": "192.168.1.170"}

# Enabled routes - choose from available_routes keys: uk, au, nz, ca, ie, il, in
enabled_route_keys = ["uk", "au", "nz", "ca", "ie", "il", "in"]

# Build routes dict from enabled keys
routes = {key: available_routes[key] for key in enabled_route_keys if key in available_routes}

# Initialize all_hosts.txt with dummy IP if it doesn't exist
all_hosts_file = alias_dir / "all_hosts.txt"
if not all_hosts_file.exists():
    with open(all_hosts_file, "w") as f:
        f.write(dummy_ip + "\n")