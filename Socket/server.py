import asyncio
import websockets

async def handle_client(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Server received your message: {message}")

start_server = websockets.serve(handle_client, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
