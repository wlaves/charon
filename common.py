# Network configuration
dummy_ip = "192.0.2.1"        # reserved IP that never expires

# Available country/region configurations
available_routes = {
    "uk": {
        "display_name": "🇬🇧 United Kingdom",
        "file_name": "uk_hosts.txt",
        "links": [
            ("BBC iPlayer", "https://www.bbc.co.uk/iplayer"),
            ("ITVX", "https://www.itv.com"),
            ("Channel 4", "https://www.channel4.com"),
            ("My5", "https://www.my5.tv"),
            ("U (UKTV Play)", "https://uktvplay.co.uk"),
            ("STV Player", "https://player.stv.tv"),
            ("S4C Clic", "https://www.s4c.cymru/clic"),
            ("All 4", "https://www.channel4.com"),
        ]
    },
    "au": {
        "display_name": "🇦🇺 Australia",
        "file_name": "au_hosts.txt",
        "links": [
            ("ABC iview", "https://iview.abc.net.au"),
            ("SBS On Demand", "https://www.sbs.com.au/ondemand"),
            ("9Now", "https://www.9now.com.au"),
            ("10 play", "https://10play.com.au"),
            ("7plus", "https://7plus.com.au"),
        ]
    },
    "nz": {
        "display_name": "🇳🇿 New Zealand",
        "file_name": "nz_hosts.txt",
        "links": [
            ("TVNZ+", "https://www.tvnz.co.nz"),
            ("ThreeNow", "https://www.threenow.co.nz"),
        ]
    },
    "ca": {
        "display_name": "🇨🇦 Canada",
        "file_name": "ca_hosts.txt",
        "links": [
            ("CBC Gem", "https://gem.cbc.ca"),
            ("CTV", "https://www.ctv.ca"),
            ("Global TV", "https://www.globaltv.com"),
        ]
    },
    "ie": {
        "display_name": "🇮🇪 Ireland",
        "file_name": "ie_hosts.txt",
        "links": [
            ("RTÉ Player", "https://www.rte.ie/player"),
            ("Virgin Media Television", "https://www.virginmediatelevision.ie/player"),
        ]
    },
    "il": {
        "display_name": "🇮🇱 Israel",
        "file_name": "il_hosts.txt",
        "links": [
            ("Kan", "https://www.kan.org.il/live/tv.aspx"),
            ("Reshet", "https://www.reshet.tv"),
        ]
    },
    "in": {
        "display_name": "🇮🇳 India",
        "file_name": "in_hosts.txt",
        "links": [
            ("Hotstar", "https://www.hotstar.com"),
            ("SonyLIV", "https://www.sonyliv.com"),
            ("Zee5", "https://www.zee5.com"),
            ("Voot", "https://www.voot.com"),
            ("MX Player", "https://www.mxplayer.in"),
            ("JioCinema", "https://www.jiocinema.com"),
            ("ALTBalaji", "https://www.altbalaji.com"),
        ]
    }
}
