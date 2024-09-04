import asyncio
import websockets

connected_clients = set()  # Keep track of connected clients

async def send_message(websocket, message):
    print("Sending message:", message)
    await websocket.send(message)

async def server(websocket, path):
    global connected_clients  # Ensure you're referencing the global set
    # Add the connected websocket client to the set
    connected_clients.add(websocket)
    print(f"New fucking client connected: {websocket.remote_address}")
    print(connected_clients)

    try:
        while True:
            # Send periodic messages to keep clients connected
            await send_message(websocket, str(connected_clients))
            await asyncio.sleep(20)
            #await send_player_message("BALLS TO THE WALL")
    except websockets.ConnectionClosed as e:
        print(f"Client disconnected: {websocket.remote_address}. Reason: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Remove the websocket client when it disconnects
        connected_clients.remove(websocket)


async def send_player_message(message: str):
    """
    Send a message to all connected players.

    Parameters
    ----------
    message : str
        The message to send to all connected players.
    """
    global connected_clients
    if connected_clients:  # Check if there are any connected clients
        print(f"Sending message to all players: {message}")
        await asyncio.gather(*[send_message(ws, message) for ws in connected_clients])
    else:
        print(connected_clients)
        print("No clients are currently connected.")

async def start_server():
    # Set up the WebSocket server
    websocket_server = websockets.serve(server, "localhost", 8765)
    async with websocket_server:
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Block here indefinitely

if __name__ == '__main__':
    asyncio.run(start_server())