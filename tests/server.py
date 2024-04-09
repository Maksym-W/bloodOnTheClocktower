from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/update_content.js':
            self.serve_js_file()
        else:
            self.serve_html_page()

    def serve_js_file(self):
        # Serve the JavaScript file
        try:
            with open('update_content.js', 'rb') as js_file:
                self.send_response(200)
                self.send_header('Content-type', 'text/javascript')
                self.end_headers()
                self.wfile.write(js_file.read())
        except FileNotFoundError:
            self.send_error(404, 'File Not Found: update_content.js')

    def serve_html_page(self):
        # Connect to SQLite database
        conn = sqlite3.connect('game.db')
        cursor = conn.cursor()

        # Fetch all roles from the database
        cursor.execute("SELECT * FROM roles")
        roles = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Generate HTML content
        html_content = '''<html><head><script src="/update_content.js"></script></head>
        <body><h1>Game Roles</h1><ul>'''

        for role in roles:
            role_name, role_description, town_allegiance = role
            html_content += f'<li><b>{role_name}</b>: {role_description} (Allegiance: {town_allegiance})</li>'
        html_content += '</ul></body></html>'

        # Serve the HTML content
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=6969):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
