from http.server import BaseHTTPRequestHandler, HTTPServer # This will be used to create an HTTP server w/ post,get
import sqlite3, os, urllib.parse
import asyncio, websockets # This will be sending out information to the clients.
from broadcaster import start_server


"""
    The below class is the HTTP server
    It has get requests for serving up the javascript/html files
    Post requests for ending the day/night.
    TODO Will probably change the post for the classes.
"""

client_count = 0

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global client_count
        if self.path == '/index.js':
            self.serve_js_file()
        elif self.path == '/client_number':
            client_count += 1
            self.send_client_number(client_count)
        else:
            self.serve_html_page()

    def do_POST(self):
        if self.path == '/end_day':
            print("End day Button is clicked")
            # Read the length of the data
            content_length = int(self.headers['Content-Length'])

            # Read the data from the request body
            post_data = self.rfile.read(content_length).decode('utf-8')

            # Print the received data
            print("Received data:", post_data)

            # Send a response back to the client
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("POST request received successfully!".encode('utf-8'))

        elif self.path == '/end_night':
            print("End night Button is clicked")
            # Read the length of the data
            content_length = int(self.headers['Content-Length'])

            # Read the data from the request body
            post_data = self.rfile.read(content_length).decode('utf-8')

            # Print the received data
            print("Received data:", post_data)

            # Send a response back to the client
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("POST request received successfully!".encode('utf-8'))
        else:
            self.send_error(404, 'File Not Found')

    def serve_js_file(self):
        # Serve the JavaScript file
        try:
            with open('frontend/client_files/index.js', 'rb') as js_file:
                self.send_response(200)
                self.send_header('Content-type', 'text/javascript')
                self.end_headers()
                self.wfile.write(js_file.read())
        except FileNotFoundError:
            self.send_error(404, 'File Not Found: client_files/index.js')

    def serve_html_page(self):
        # Get the current directory
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Navigate to the client_files directory
        client_files_directory = os.path.join(os.path.dirname(__file__), '../frontend/client_files')

        # Read the content of index.html
        index_html_path = os.path.join(client_files_directory, 'index.html')
        with open(index_html_path, 'r') as file:
            html_content = file.read()

        # Serve the HTML content
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

    def send_client_number(self, client_number):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(f'{{"client_number": {client_number}}}'.encode('utf-8'))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    
    httpd.serve_forever()


if __name__ == '__main__':
    run()
