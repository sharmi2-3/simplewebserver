from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<body>
<h1>configuration:24900072</h1>
<ol>
<li>Device name	DESKTOP-AJ75N8I</li>
<li>Processor	AMD Ryzen 3 3200U with Radeon Vega Mobile Gfx     2.60 GHz</li>
<li>Installed RAM	8.00 GB (5.95 GB usable)</li>
<li>Device ID	A5B41A09-4EF7-460F-BDE4-BCA0BE051A1A</li>
<li>Product ID	00331-10000-00001-AA266</li>
<li>System type	64-bit operating system, x64-based processor</li>
<li>Pen and touch No pen or touch input is available for this display</li>
</ol>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()