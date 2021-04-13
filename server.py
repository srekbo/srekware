#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import ssl

import config as c

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"BaUmKuChEn IsT leCkEr")
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        print(self.path)
httpd = HTTPServer(("0.0.0.0", 4443), RequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=c.get("server.certs.key"), certfile=c.get("server.certs.chain"), server_side=True)
print("StartServer")
try:
    httpd.serve_forever()
except:
    pass
