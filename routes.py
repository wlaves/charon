from flask import request, jsonify, send_from_directory
from models import load_state, add_ip, remove_ip, valid_ip, client_ip, set_ip_route, clear_all_routes
from config import ALIAS_DIR, TV_IP, DUMMY_IP, ROUTES
import json

def register_routes(app):
    @app.get("/")
    def index():
        route_options = ""
        for route_key, route_config in ROUTES.items():
            route_options += f'<option value="{route_key}">{route_config["display_name"]}</option>'
        
        return f"""
<!doctype html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>brittv</title></head>
<body style="font-family:system-ui;margin:2rem;max-width:40rem">
<h1>brittv</h1>
<label>tv: <select id="tv">
  <option value="disabled">Disabled</option>
  {route_options}
</select></label>
<br><br>
<label>self ({client_ip(request)}): <select id="self">
  <option value="disabled">Disabled</option>
  {route_options}
</select></label>
<br><br>
<h3>Routed:</h3>
<div id="routed"></div>
<br>
<button id="clearAll" style="padding:0.5rem 1rem;background:#dc3545;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold">Clear All</button>
<br><br>
<div id="links"></div>
<script>
const ROUTES = {json.dumps(ROUTES)};

async function getState() {{
  const r = await fetch("/state");
  const s = await r.json();
  const selfIp = "{client_ip(request)}";
  document.getElementById("tv").value = s.tv || "disabled";
  document.getElementById("self").value = s.self || "disabled";
  const routedDiv = document.getElementById("routed");
  routedDiv.innerHTML = "";
  Object.entries(s.list).forEach(([ip, route]) => {{
    if (ip === "{DUMMY_IP}" || ip === "{TV_IP}" || ip === selfIp) return; // hide dummy, tv, self
    const label = document.createElement("label");
    const select = document.createElement("select");
    select.innerHTML = '<option value="disabled">Disabled</option>{route_options}';
    select.value = route || "disabled";
    select.addEventListener("change", e => setToggle(ip, e.target.value));
    label.appendChild(document.createTextNode(ip + ": "));
    label.appendChild(select);
    routedDiv.appendChild(label);
    routedDiv.appendChild(document.createElement("br"));
  }});
  updateLinks();
}}

function updateLinks() {{
  const selfRoute = document.getElementById("self").value;
  const linksDiv = document.getElementById("links");
  linksDiv.innerHTML = "";
  
  // Only show links for Self route
  if (selfRoute !== "disabled" && ROUTES[selfRoute] && ROUTES[selfRoute].links && ROUTES[selfRoute].links.length > 0) {{
    const header = document.createElement("h4");
    header.textContent = ROUTES[selfRoute].display_name;
    header.style.fontWeight = "bold";
    header.style.marginBottom = "0.5rem";
    linksDiv.appendChild(header);
    
    const list = document.createElement("ul");
    list.style.marginTop = "0";
    list.style.marginBottom = "1rem";
    
    ROUTES[selfRoute].links.forEach(linkData => {{
      const name = linkData[0];
      const url = linkData[1];
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = url.startsWith("http") ? url : "https://" + url;
      link.textContent = name;
      link.target = "_blank";
      item.appendChild(link);
      list.appendChild(item);
    }});
    
    linksDiv.appendChild(list);
  }}
}}

async function setToggle(name, route) {{
  await fetch("/toggle", {{
    method: "POST",
    headers: {{ "Content-Type": "application/json" }},
    body: JSON.stringify({{ name, route }})
  }});
  await getState();
}}

async function clearAll() {{
  if (confirm("Clear all routes? This will reset all files to only contain the dummy IP.")) {{
    await fetch("/clear", {{ method: "POST" }});
    await getState();
  }}
}}

document.getElementById("tv").addEventListener("change", e => {{
  setToggle("tv", e.target.value);
}});
document.getElementById("self").addEventListener("change", e => {{
  setToggle("self", e.target.value);
  updateLinks();
}});
document.getElementById("clearAll").addEventListener("click", clearAll);
getState();
</script>
</body>
</html>
"""

    @app.get("/state")
    def state():
        state = load_state()
        me = client_ip(request)
        tv_route = state.get(TV_IP, {}).get("route") if TV_IP in state else None
        self_route = state.get(me, {}).get("route") if me in state else None
        
        # Convert state to route mapping for frontend
        list_with_routes = {}
        for ip, data in state.items():
            list_with_routes[ip] = data.get("route")
        
        return jsonify({
            "tv": tv_route,
            "self": self_route,
            "list": list_with_routes
        })

    @app.post("/toggle")
    def toggle():
        data = request.get_json(force=True)
        name = data.get("name")
        route = data.get("route")

        if name == "tv":
            set_ip_route(TV_IP, route)
        elif name == "self":
            me = client_ip(request)
            if not valid_ip(me):
                return ("bad ip", 400)
            set_ip_route(me, route)
        elif valid_ip(name):
            set_ip_route(name, route)
        else:
            return ("bad toggle", 400)
        return ("ok", 200)

    @app.post("/clear")
    def clear():
        clear_all_routes()
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

