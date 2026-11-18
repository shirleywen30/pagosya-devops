import http.server, pathlib
VERSION = pathlib.Path("/app/VERSION").read_text().strip()

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = b"ok\n"
        else:
            body = f"PagosYA api {VERSION}\n".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *args):
        pass

http.server.HTTPServer(("0.0.0.0", 9000), Handler).serve_forever()
