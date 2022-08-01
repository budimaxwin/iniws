import asyncio
import json
import websockets
import logging

logging.basicConfig(level=logging.DEBUG)

def pong(text):
    return '{"message":"' + text + '"}'

async def handler(websocket):
    while True:
        j_message = {}
        message = await websocket.recv()
        try:
            j_message = json.loads(message)
            action = j_message['action']

            if action=='get_group_id':
                print(action)

        except KeyError:
            await websocket.send(pong('error'))
        except json.JSONDecodeError:
            await websocket.send(pong('JSON-like data is required'))




async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())