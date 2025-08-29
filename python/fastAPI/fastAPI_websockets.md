
Nice tip: use connection manager for websockets

```python
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    await manager.broadcast("Someone joined")
    try:
        while True:
           
            message = await websocket.receive_text()
            await websocket.send_json({'msg':message})
            await asyncio.sleep(2)
            await websocket.send_json({'msg': 'pong'})
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat..")
    except Exception as e:
        await manager.broadcast(f"{str(e)}")
        manager.disconnect(websocket)
```