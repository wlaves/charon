# Network configuration
dummy_ip = "192.0.2.1"        # reserved IP that never expires

# Available country/region configurations
available_routes = {
    "ae": {
        "display_name": "🇦🇪 United Arab Emirates",
        "file_name": "ae_hosts.txt",
        "links": [
            ("ADtv", "https://adtv.ae")
        ]
    },
    # "ar" entry removed (Cont.ar service was shut down in 2024)
    "at": {
        "display_name": "🇦🇹 Austria",
        "file_name": "at_hosts.txt",
        "links": [
            ("ORF TVthek", "https://tvthek.orf.at")
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
            ("7plus", "https://7plus.com.au")
        ]
    },
    "ba": {
        "display_name": "🇧🇦 Bosnia and Herzegovina",
        "file_name": "ba_hosts.txt",
        "links": [
            ("BHRT (BHT)", "https://www.bhrt.ba")
        ]
    },
    "be": {
        "display_name": "🇧🇪 Belgium",
        "file_name": "be_hosts.txt",
        "links": [
            ("VRT MAX", "https://www.vrt.be/vrtmax"),
            ("RTBF Auvio", "https://auvio.rtbf.be")
        ]
    },
    "bg": {
        "display_name": "🇧🇬 Bulgaria",
        "file_name": "bg_hosts.txt",
        "links": [
            ("BNT", "https://bnt.bg"),
            ("bTV Plus", "https://btvplus.bg"),
            ("Nova Play", "https://play.nova.bg")
        ]
    },
    "br": {
        "display_name": "🇧🇷 Brazil",
        "file_name": "br_hosts.txt",
        "links": [
            ("Globoplay (Free)", "https://globoplay.globo.com"),
            ("PlayPlus", "https://www.playplus.com")
        ]
    },
    "ca": {
        "display_name": "🇨🇦 Canada",
        "file_name": "ca_hosts.txt",
        "links": [
            ("CBC Gem", "https://gem.cbc.ca"),
            ("CTV", "https://www.ctv.ca"),
            ("Global TV", "https://www.globaltv.com")
        ]
    },
    "ch": {
        "display_name": "🇨🇭 Switzerland",
        "file_name": "ch_hosts.txt",
        "links": [
            ("Play SRF", "https://www.srf.ch/play"),
            ("Play RTS", "https://www.rts.ch/play"),
            ("Play RSI", "https://www.rsi.ch/play")
        ]
    },
    "cl": {
        "display_name": "🇨🇱 Chile",
        "file_name": "cl_hosts.txt",
        "links": [
            ("TVN Play", "https://www.tvnplay.com"),
            ("CNTV Play", "https://www.cntvplay.cl")
        ]
    },
    "de": {
        "display_name": "🇩🇪 Germany",
        "file_name": "de_hosts.txt",
        "links": [
            ("ARD Mediathek", "https://www.ardmediathek.de"),
            ("ZDF Mediathek", "https://www.zdf.de/mediathek"),
            ("Joyn", "https://www.joyn.de")
        ]
    },
    "dk": {
        "display_name": "🇩🇰 Denmark",
        "file_name": "dk_hosts.txt",
        "links": [
            ("DR TV", "https://www.dr.dk/drtv")
        ]
    },
    "ee": {
        "display_name": "🇪🇪 Estonia",
        "file_name": "ee_hosts.txt",
        "links": [
            ("Jupiter (ERR)", "https://jupiter.err.ee")
        ]
    },
    "eg": {
        "display_name": "🇪🇬 Egypt",
        "file_name": "eg_hosts.txt",
        "links": [
            ("Shahid (MBC)", "https://shahid.mbc.net")
        ]
    },
    "fi": {
        "display_name": "🇫🇮 Finland",
        "file_name": "fi_hosts.txt",
        "links": [
            ("Yle Areena", "https://areena.yle.fi")
        ]
    },
    "fr": {
        "display_name": "🇫🇷 France",
        "file_name": "fr_hosts.txt",
        "links": [
            ("France.tv", "https://www.france.tv"),
            ("MyTF1", "https://www.mytf1.fr"),
            ("6play", "https://www.6play.fr")
        ]
    },
    "gr": {
        "display_name": "🇬🇷 Greece",
        "file_name": "gr_hosts.txt",
        "links": [
            ("ERTFLIX", "https://www.ertflix.gr")
        ]
    },
    "hk": {
        "display_name": "🇭🇰 Hong Kong",
        "file_name": "hk_hosts.txt",
        "links": [
            ("myTV Super (TVB)", "https://www.mytvsuper.com")
        ]
    },
    "hu": {
        "display_name": "🇭🇺 Hungary",
        "file_name": "hu_hosts.txt",
        "links": [
            ("Mediaklikk", "https://mediaklikk.hu")
        ]
    },
    "id": {
        "display_name": "🇮🇩 Indonesia",
        "file_name": "id_hosts.txt",
        "links": [
            ("Vidio", "https://www.vidio.com"),
            ("RCTI+", "https://www.rctiplus.com")
        ]
    },
    "ie": {
        "display_name": "🇮🇪 Ireland",
        "file_name": "ie_hosts.txt",
        "links": [
            ("RTÉ Player", "https://www.rte.ie/player"),
            ("Virgin Media Television", "https://www.virginmediatelevision.ie/player")
        ]
    },
    "il": {
        "display_name": "🇮🇱 Israel",
        "file_name": "il_hosts.txt",
        "links": [
            ("Kan", "https://www.kan.org.il/lobby/kan-box/"),
            ("Reshet 13", "https://13tv.co.il")
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
            ("JioCinema", "https://www.jiocinema.com")
            # ALTBalaji removed (service banned in 2025)
        ]
    },
    "is": {
        "display_name": "🇮🇸 Iceland",
        "file_name": "is_hosts.txt",
        "links": [
            ("RÚV", "https://www.ruv.is")
        ]
    },
    "it": {
        "display_name": "🇮🇹 Italy",
        "file_name": "it_hosts.txt",
        "links": [
            ("RaiPlay", "https://raiplay.it"),
            ("Mediaset Infinity", "https://mediasetinfinity.mediaset.it")
        ]
    },
    "jp": {
        "display_name": "🇯🇵 Japan",
        "file_name": "jp_hosts.txt",
        "links": [
            ("NHK Plus", "https://plus.nhk.jp"),
            ("TVer", "https://tver.jp")
        ]
    },
    "kr": {
        "display_name": "🇰🇷 South Korea",
        "file_name": "kr_hosts.txt",
        "links": [
            ("KBS (온에어/VOD)", "https://www.kbs.co.kr"),
            ("Wavve", "https://www.wavve.com")
        ]
    },
    "lb": {
        "display_name": "🇱🇧 Lebanon",
        "file_name": "lb_hosts.txt",
        "links": [
            ("LBCI", "https://www.lbcgroup.tv/shows/en"),
            ("MTV Lebanon", "https://www.mtv.com.lb/vod")
        ]
    },
    "lk": {
        "display_name": "🇱🇰 Sri Lanka",
        "file_name": "lk_hosts.txt",
        "links": [
            ("Rupavahini", "http://tv.rupavahini.lk")
        ]
    },
    "lt": {
        "display_name": "🇱🇹 Lithuania",
        "file_name": "lt_hosts.txt",
        "links": [
            ("LRT Mediateka", "https://www.lrt.lt/mediateka")
        ]
    },
    "lv": {
        "display_name": "🇱🇻 Latvia",
        "file_name": "lv_hosts.txt",
        "links": [
            ("LSM RePlay", "https://replay.lsm.lv")
        ]
    },
    "ma": {
        "display_name": "🇲🇦 Morocco",
        "file_name": "ma_hosts.txt",
        "links": [
            ("SNRT Live/Replay", "https://snrtlive.ma")
        ]
    },
    "mt": {
        "display_name": "🇲🇹 Malta",
        "file_name": "mt_hosts.txt",
        "links": [
            ("TVM", "https://www.tvm.com.mt")
        ]
    },
    "mx": {
        "display_name": "🇲🇽 Mexico",
        "file_name": "mx_hosts.txt",
        "links": [
            ("Vix", "https://vix.com")
        ]
    },
    "nl": {
        "display_name": "🇳🇱 Netherlands",
        "file_name": "nl_hosts.txt",
        "links": [
            ("NPO Start", "https://www.npostart.nl"),
            ("KIJK", "https://www.kijk.nl")
        ]
    },
    "no": {
        "display_name": "🇳🇴 Norway",
        "file_name": "no_hosts.txt",
        "links": [
            ("NRK TV", "https://tv.nrk.no")
        ]
    },
    "nz": {
        "display_name": "🇳🇿 New Zealand",
        "file_name": "nz_hosts.txt",
        "links": [
            ("TVNZ+", "https://www.tvnz.co.nz"),
            ("ThreeNow", "https://www.threenow.co.nz")
        ]
    },
    "pe": {
        "display_name": "🇵🇪 Peru",
        "file_name": "pe_hosts.txt",
        "links": [
            ("TV Perú Play", "https://play.tvperu.gob.pe"),
            ("América TVGo", "https://tvgo.americatv.com.pe")
        ]
    },
    "ph": {
        "display_name": "🇵🇭 Philippines",
        "file_name": "ph_hosts.txt",
        "links": [
            ("iWantTFC", "https://www.iwanttfc.com")
        ]
    },
    "pk": {
        "display_name": "🇵🇰 Pakistan",
        "file_name": "pk_hosts.txt",
        "links": [
            ("PTV Flix", "https://ptvflix.com.pk"),
            ("ARY ZAP", "https://www.aryzap.com")
        ]
    },
    "pl": {
        "display_name": "🇵🇱 Poland",
        "file_name": "pl_hosts.txt",
        "links": [
            ("TVP VOD", "https://vod.tvp.pl"),
            ("Player.pl", "https://player.pl")
        ]
    },
    "pt": {
        "display_name": "🇵🇹 Portugal",
        "file_name": "pt_hosts.txt",
        "links": [
            ("RTP Play", "https://www.rtp.pt/play"),
            ("TVI Player", "https://tviplayer.iol.pt")
        ]
    },
    "qa": {
        "display_name": "🇶🇦 Qatar",
        "file_name": "qa_hosts.txt",
        "links": [
            ("Al Jazeera", "https://www.aljazeera.net")
        ]
    },
    "rs": {
        "display_name": "🇷🇸 Serbia",
        "file_name": "rs_hosts.txt",
        "links": [
            ("RTS Planeta", "https://rtsplaneta.rs")
        ]
    },
    "ru": {
        "display_name": "🇷🇺 Russia",
        "file_name": "ru_hosts.txt",
        "links": [
            ("Smotrim", "https://smotrim.ru"),
            ("Channel One (1tv)", "https://www.1tv.ru")
        ]
    },
    "se": {
        "display_name": "🇸🇪 Sweden",
        "file_name": "se_hosts.txt",
        "links": [
            ("SVT Play", "https://www.svtplay.se"),
            ("TV4 Play", "https://www.tv4play.se")
        ]
    },
    "sg": {
        "display_name": "🇸🇬 Singapore",
        "file_name": "sg_hosts.txt",
        "links": [
            ("meWATCH", "https://www.mewatch.sg")
        ]
    },
    "si": {
        "display_name": "🇸🇮 Slovenia",
        "file_name": "si_hosts.txt",
        "links": [
            ("RTV 365 (RTV SLO)", "https://365.rtvslo.si")
        ]
    },
    "sk": {
        "display_name": "🇸🇰 Slovakia",
        "file_name": "sk_hosts.txt",
        "links": [
            ("RTVS", "https://www.rtvs.sk")
        ]
    },
    "sv": {
        "display_name": "🇸🇻 El Salvador",
        "file_name": "sv_hosts.txt",
        "links": [
            ("TCS Go", "https://www.tcsgo.com")
        ]
    },
    "th": {
        "display_name": "🇹🇭 Thailand",
        "file_name": "th_hosts.txt",
        "links": [
            ("CH3Plus", "https://ch3plus.com"),
            ("Bugaboo.tv", "https://www.bugaboo.tv")
        ]
    },
    "tw": {
        "display_name": "🇹🇼 Taiwan",
        "file_name": "tw_hosts.txt",
        "links": [
            ("PTS", "https://www.pts.org.tw")
        ]
    },
    "ua": {
        "display_name": "🇺🇦 Ukraine",
        "file_name": "ua_hosts.txt",
        "links": [
            ("Suspilne (UA:PBC)", "https://suspilne.media"),
            ("1+1 Video", "https://1plus1.video")
        ]
    },
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
            ("S4C Clic", "https://www.s4c.cymru/clic")
            # "All 4" removed (merged into Channel 4 brand)
        ]
    },
    "vn": {
        "display_name": "🇻🇳 Vietnam",
        "file_name": "vn_hosts.txt",
        "links": [
            ("VTV Go", "https://vtvgo.vn")
        ]
    },
    "za": {
        "display_name": "🇿🇦 South Africa",
        "file_name": "za_hosts.txt",
        "links": [
            ("SABC+ (SABC)", "https://sabc-plus.com"),
            ("eVOD", "https://watch.evod.co.za")
        ]
    }
}
