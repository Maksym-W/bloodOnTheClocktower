import asyncio
import websockets

async def send_message(websocket, message):
    print("Sending message:", message)
    await websocket.send(message)

async def server(websocket, path):
    while True:
        await send_message(websocket, "we confirm this works")
        await asyncio.sleep(3)  # Sends message every 3 seconds

async def start_server():
    # Set up the WebSocket server
    websocket_server = websockets.serve(server, "localhost", 8765)
    async with websocket_server:
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Block here indefinitely

if __name__ == '__main__':
    asyncio.run(start_server())