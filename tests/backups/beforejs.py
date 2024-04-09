from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Connect to SQLite database
        conn = sqlite3.connect('game.db')
        cursor = conn.cursor()

        # Fetch all roles from the database
        cursor.execute("SELECT * FROM roles")
        roles = cursor.fetchall()

        # Generate HTML content with embedded JavaScript
        html_content = '''<html><head><script>
        setTimeout(function() {
            var testText = document.createElement("h6");
            testText.innerHTML = "this is a test";
            document.body.appendChild(testText);
        }, 3000);
        </script></head><body><h1>Game Roles</h1><ul>'''

        for role in roles:
            role_name, role_description, town_allegiance = role
            html_content += f'<li><b>{role_name}</b>: {role_description} (Allegiance: {town_allegiance})</li>'
        html_content += '</ul></body></html>'

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

        # Close the database connection
        conn.close()

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=6969):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

