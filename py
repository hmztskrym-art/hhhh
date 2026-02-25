from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 3000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
        <head>
            <title>منظومة محل</title>
        </head>
        <body style="text-align:center; font-family:Arial;">
            <h1>منظومة المحل شغالة ✅</h1>
            <p>المشروع يعمل بدون Flask وبدون تحميل أي مكتبة</p>
        </body>
        </html>
        """

        self.wfile.write(html.encode())

print("Server running on port", PORT)
server = HTTPServer(("0.0.0.0", PORT), MyHandler)
server.serve_forever()
