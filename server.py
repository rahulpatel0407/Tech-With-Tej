import http.server
import socketserver

PORT = 8080

class UTF8Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Force UTF-8 for HTML files
        if self.path.endswith('.html') or self.path.endswith('/') or '.' not in self.path.split('/')[-1]:
            self.send_header('Content-Type', 'text/html; charset=utf-8')
        super().end_headers()
    
    def guess_type(self, path):
        ctype = super().guess_type(path)
        if 'text/html' in ctype:
            return 'text/html; charset=utf-8'
        return ctype
    
    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}")

with socketserver.TCPServer(("", PORT), UTF8Handler) as httpd:
    print(f"Portfolio server running at http://localhost:{PORT}/")
    print(f"Open: http://localhost:{PORT}/portfolio-preview%20(2).html")
    httpd.serve_forever()
