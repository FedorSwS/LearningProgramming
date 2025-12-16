from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
import uuid
import os

app = FastAPI()

active_connections = []
chat_history = []

FILE = os.path.join(os.path.dirname(__file__), "chat.html")

@app.get("/")
async def get():
    with open(FILE, "r", encoding="utf-8") as f:
        html = f.read()
        return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    user_id = str(uuid.uuid4())[:8]
    active_connections.append((websocket, user_id))

    for msg in chat_history:
        await websocket.send_text(msg)
    
    try:
        while True:
            data = await websocket.receive_text()
            message = f"[Пользователь {user_id}]: {data}"
            
            chat_history.append(message)
            for connection, i in active_connections:
                await connection.send_text(message)
    except Exception:
        active_connections[:] = [(conn, uid) for conn, uid in active_connections if conn != websocket]

if __name__=="__main__":
    uvicorn.run("Variant_5_6:app", host="127.0.0.1", port=5001, reload=True)