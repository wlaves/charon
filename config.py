from pathlib import Path

# Directory and file paths
ALIAS_DIR = Path("/var/www/alias")
ALIAS_DIR.mkdir(parents=True, exist_ok=True)
STATE_FILE = ALIAS_DIR / "state.json"

# Network configuration
TV_IP = "192.168.1.170"       # set your Smart TV's IP
DUMMY_IP = "192.0.2.1"        # reserved IP that never expires

# Routing configuration
ROUTES = {
    "uk": {
        "display_name": "UK",
        "file_name": "brittv_hosts.txt",
        "links": [
            ("BBC iPlayer", "https://bbc.co.uk/iplayer"),
            ("ITV Hub", "https://itv.com/hub"),
            ("Channel 4", "https://channel4.com"),
        ]
    }
}

