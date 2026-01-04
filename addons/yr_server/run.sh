#!/usr/bin/with-contenv bashio

# Lag venv i /data og aktiver det
python3 -m venv /data/venv
. /data/venv/bin/activate

# Oppdater pip og installer requests i venv
pip install --upgrade pip
pip install requests

# Start Python-serveren
exec /data/venv/bin/python /data/server.py
