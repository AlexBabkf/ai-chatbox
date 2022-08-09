from fatapi import WebSocket

class ConnectionManger:
    def __init__(self):
        self.active_connections: List[WebSocket] = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
