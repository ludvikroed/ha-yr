from http.server import HTTPServer, SimpleHTTPRequestHandler
import requests
import urllib.parse
import json

PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/weather"):
            # Hent query params
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            lat = params.get("lat", [None])[0]
            lon = params.get("lon", [None])[0]

            if not lat or not lon:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Mangler lat eller lon"}).encode())
                return

            try:
                url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
                headers = {"User-Agent": "MinVærApp/1.0 kontakt@eksempel.no"}
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                data = response.json()

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())

            except Exception as e:
                print("Feil:", e)
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Kunne ikke hente værdata fra YR"}).encode())

        else:
            # Serve index.html eller andre filer fra public/
            if self.path == "/":
                self.path = "/index.html"
            self.path = "/public" + self.path
            return SimpleHTTPRequestHandler.do_GET(self)

httpd = HTTPServer(("0.0.0.0", PORT), MyHandler)
print(f"Server kjører på port {PORT}")
httpd.serve_forever()
