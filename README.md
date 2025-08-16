# Charon - Geo-unlocking Route Manager

Charon is a Flask-based web application for managing IP routing through different geographic locations to unlock geo-restricted content. It provides a simple web interface to route devices (TV, self, and other IPs) through various country-specific proxy endpoints.

## Features

- **Web Interface**: Simple, responsive web UI for managing routes
- **Multiple Countries**: Support for 50+ countries and regions
- **Device Management**: Separate routing for TV, self (your current IP), and other discovered devices
- **File-based Output**: Generates host files for each country/region
- **Automatic Discovery**: Tracks and manages IPs that connect to the service
- **Clear All**: Reset all routes with a single button
- **Links Integration**: Shows relevant streaming service links for selected regions

## Architecture

```
/opt/charon/
├── app.py              # Flask application entry point
├── routes.py           # Web routes and HTML interface
├── models.py           # Business logic and file management
├── config.py           # Local configuration (gitignored)
├── config.py.template  # Configuration template
├── common.py           # Shared country definitions
└── README.md           # This file
```

## Installation

1. **Clone and setup**:
   ```bash
   cd /opt
   git clone <repository> charon
   cd charon
   ```

2. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install flask
   ```

3. **Configure application**:
   ```bash
   cp config.py.template config.py
   # Edit config.py to customize your setup
   ```

4. **Create systemd service** (optional):
   ```bash
   # Create /etc/systemd/system/charon.service
   sudo systemctl enable charon
   sudo systemctl start charon
   ```

## Configuration

Edit `config.py` to customize your setup:

### TV Configuration
```python
tv_ip = {"Living Room TV": "192.168.1.170"}
```

### Country Selection
Choose which countries to enable:
```python
enabled_route_keys = ["uk", "au", "nz", "ca", "ie"]
```

Available countries include:
- `uk` - United Kingdom (BBC iPlayer, ITVX, Channel 4, etc.)
- `au` - Australia (ABC iview, SBS, 9Now, etc.)
- `ca` - Canada (CBC Gem, CTV, Global TV)
- `ie` - Ireland (RTÉ Player, Virgin Media)
- `de` - Germany (ARD, ZDF, Joyn)
- `fr` - France (France.tv, MyTF1, 6play)
- `jp` - Japan (NHK Plus, TVer)
- ...and 40+ more countries

## Usage

### Web Interface

1. **Access the interface**: `http://localhost:5000`

2. **Configure devices**:
   - **TV dropdown**: Select country for your TV's routing
   - **Self dropdown**: Select country for your current IP
   - **Routed section**: Manage other discovered IPs

3. **View links**: When you select a country for "Self", relevant streaming service links appear at the bottom

4. **Clear all**: Reset all routing to default (dummy IP only)

### API Endpoints

- `GET /state` - Get current routing state
- `POST /toggle` - Change device routing
- `POST /clear` - Clear all routes
- `GET /alias/<filename>` - Download generated host files
- `GET /debugip` - Debug IP detection

### Generated Files

The application generates host files in `/var/www/alias/`:
- `<country>_hosts.txt` - IPs routed through specific country
- `all_hosts.txt` - All routed IPs combined
- `state.json` - Current application state

## Host File Format

Each generated host file contains one IP per line:
```
192.0.2.1
192.168.1.170
192.168.1.100
```

The dummy IP (`192.0.2.1`) is always included to ensure files are never empty.

## Integration

### Nginx/Proxy Integration

Host files can be consumed by:
- Nginx upstream configurations
- HAProxy backends  
- DNS override lists
- Firewall routing rules

Example nginx upstream:
```nginx
upstream uk_backend {
    include /var/www/alias/uk_hosts.txt;
}
```

### Systemd Service

Example service file (`/etc/systemd/system/charon.service`):
```ini
[Unit]
Description=Charon Geo-unlock Route Manager
After=network.target

[Service]
Type=exec
User=www-data
WorkingDirectory=/opt/charon
Environment=PATH=/opt/charon/venv/bin
ExecStart=/opt/charon/venv/bin/gunicorn -w 2 -b 127.0.0.1:5000 app:APP
Restart=always

[Install]
WantedBy=multi-user.target
```

## Development

### File Structure

- **app.py**: Flask application factory and main entry point
- **routes.py**: Web routes, HTML generation, and request handling
- **models.py**: Business logic, file I/O, and state management
- **config.py**: Local configuration (TV IPs, enabled countries)
- **common.py**: Shared country/region definitions and constants

### Adding Countries

1. Add country definition to `common.py`:
   ```python
   "xx": {
       "display_name": "🇽🇽 Country Name",
       "file_name": "xx_hosts.txt",
       "links": [
           ("Service Name", "https://service.example.com")
       ]
   }
   ```

2. Add country code to your `config.py`:
   ```python
   enabled_route_keys = ["uk", "au", "xx"]
   ```

### IP Detection

The application detects client IPs using:
1. `X-Real-IP` header (nginx)
2. `X-Forwarded-For` header (proxies)
3. `request.remote_addr` (direct connection)

## Security Considerations

- The application runs on localhost by default
- No authentication is implemented - intended for internal networks
- Generated files are world-readable in `/var/www/alias/`
- Consider firewall rules if exposing externally

## Troubleshooting

### Application won't start
- Check virtual environment activation
- Verify Flask installation: `pip list | grep -i flask`
- Check port availability: `netstat -ln | grep :5000`

### Files not generating
- Verify `/var/www/alias/` directory permissions
- Check application logs for file write errors
- Ensure sufficient disk space

### IP detection issues
- Check `/debugip` endpoint for header inspection
- Verify proxy configuration (X-Real-IP headers)
- Test from different network locations

### Configuration errors
- Validate `config.py` syntax: `python -m py_compile config.py`
- Check enabled country codes against `common.py`
- Verify TV IP format (must be valid IPv4)

