from http.server import BaseHTTPRequestHandler, HTTPServer # This will be used to create an HTTP server w/ post,get
import sqlite3, os, urllib.parse
import asyncio, websockets # This will be sending out information to the clients.
from broadcaster import start_server, send_player_message
import game_rules.game_logic


"""
    The below class is the HTTP server
    It has get requests for serving up the javascript/html files
    Post requests for ending the day/night.
    TODO Will probably change the post for the classes.
"""

client_count = 0
clients = [] # TODO rewrite the code such that whenever client_count is used, len(clients) is used instead.
game_master = None

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global client_count, clients

        if self.client_address[0] not in clients:
            clients.append(self.client_address[0])

        if self.path == '/index.js':
            self.serve_js_file()
        elif self.path == '/client_number':
            client_count += 1
            self.send_client_number(client_count)
        else:
            self.serve_html_page()

    def do_POST(self):
        global game_master

        # TODO Determine if we need to register clients here.

        if self.path == '/master':
            print("End day Button is clicked")
            if game_master == None:
                game_master = self.client_address[0]
                print("The game master is: " + game_master)
            else:
                print(self.client_address[0] + " tried to be the game master.")
            
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
            self.wfile.write("POST request received successfully! You are the game master".encode('utf-8'))

        elif self.path == '/player':
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
            self.wfile.write("You have not been assigned a player role yet".encode('utf-8'))

        elif self.path == '/masterSet':
            print("MasterSet Button is clicked")

            # Read the length of the data
            content_length = int(self.headers['Content-Length'])

            # Read the data from the request body
            post_data = self.rfile.read(content_length).decode('utf-8')

            # Print the received data
            print("Received data:", post_data)

            # Set up the game
            game_instance = setup_game()

            # Tell the players their roles. TODO use the broadcaster.
            asyncio.run(send_player_message("Game setup complete. You have been assigned roles.")) # TODO TO FIX THIS, WE NEED TO PASS IN THE CLIENTS INTO HERE. 
            print(clients)
            print("----------------------------------------------")

            # Send a response back to the client
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("hello there".encode('utf-8'))

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


def setup_game():
    # TODO Given the number of players in the game, give each player a random role.
    game_instance = game_rules.game_logic.game(client_count)
    game_instance.assign_roles()
    return game_instance

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8001):

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    
    httpd.serve_forever()


if __name__ == '__main__':
    run()
