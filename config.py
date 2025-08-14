from pathlib import Path

# Directory and file paths
ALIAS_DIR = Path("/var/www/alias")
ALIAS_DIR.mkdir(parents=True, exist_ok=True)
LIST_FILE = ALIAS_DIR / "brittv_hosts.txt"
STATE_FILE = ALIAS_DIR / "state.json"

# Network configuration
TV_IP = "192.168.1.170"       # set your Smart TV's IP
DUMMY_IP = "192.0.2.1"        # reserved IP that never expires
EXPIRY_SECONDS = 6 * 3600     # 6 hours
