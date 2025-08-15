from pathlib import Path

# Directory and file paths
alias_dir = Path("/var/www/alias")
alias_dir.mkdir(parents=True, exist_ok=True)
state_file = alias_dir / "state.json"

# Network configuration
tv_ip = "192.168.1.170"       # set your Smart TV's IP
dummy_ip = "192.0.2.1"        # reserved IP that never expires

# Routing configuration
routes = {
    "uk": {
        "display_name": "🇬🇧 United Kingdom",
        "file_name": "uk_hosts.txt",
        "links": [
            ("BBC iPlayer", "https://bbc.co.uk/iplayer"),
            ("ITVX", "https://itv.com"),
            ("Channel 4", "https://channel4.com"),
            ("My5", "https://my5.tv"),
            ("U (UKTV Play)", "https://u.co.uk"),
            ("STV Player", "https://player.stv.tv"),
            ("S4C Clic", "https://s4c.cymru/clic"),
            ("All 4", "https://channel4.com"),
        ]
    },
    "au": {
        "display_name": "🇦🇺 Australia", 
        "file_name": "au_hosts.txt",
        "links": [
            ("ABC iview", "https://iview.abc.net.au"),
            ("SBS On Demand", "https://sbs.com.au/ondemand"),
            ("9Now", "https://9now.com.au"),
            ("10 play", "https://10play.com.au"),
            ("7plus", "https://7plus.com.au"),
        ]
    },
    "nz": {
        "display_name": "🇳🇿 New Zealand",
        "file_name": "nz_hosts.txt", 
        "links": [
            ("TVNZ+", "https://tvnz.co.nz/ondemand"),
            ("ThreeNow", "https://threenow.co.nz"),
        ]
    },
    "ca": {
        "display_name": "🇨🇦 Canada",
        "file_name": "ca_hosts.txt",
        "links": [
            ("CBC Gem", "https://gem.cbc.ca"),
            ("CTV", "https://ctv.ca"),
            ("Global TV", "https://globaltv.com"),
        ]
    },
    "ie": {
        "display_name": "🇮🇪 Ireland", 
        "file_name": "ie_hosts.txt",
        "links": [
            ("RTÉ Player", "https://rte.ie/player"),
            ("Virgin Media Television", "https://virginmediatelevision.ie"),
        ]
    },
    "il": {
        "display_name": "🇮🇱 Israel",
        "file_name": "il_hosts.txt",
        "links": [
            ("Kan", "https://kan.org.il"),
            ("Reshet", "https://reshet.tv"),
        ]
    }
}

# Initialize all_hosts.txt with dummy IP if it doesn't exist
all_hosts_file = alias_dir / "all_hosts.txt"
if not all_hosts_file.exists():
    with open(all_hosts_file, "w") as f:
        f.write(dummy_ip + "\n")