import os
from fastapi import APIRouter, FastAPI, WebSocket, Request
import uuid

chat = APIRouter()

# @route POST /token
# @desc Route to generate chat token
# @access Public

@chat.post("/token")
async def token_generator(request: Request):

    if name == "":
        raise HTTPException(
            status_code = 400, 
            detail = {
            "loc": "name", "msg": "Enter a valid name"
        })

    token = str(uuid.uuid4())

    data = {"name": name, "token": token}

    return data


# @route POST /refresh_token
# @desc Route to refresh token
# @access Public

@chat.post("/refresh_token")
async def refresh_token(request: Request):
    return None


# @route Websocket /chat
# @desc Socket for chatbot
# @access Public

@chat.post("/chat")
async def websocket_endpoint(websocket: WebSocket = WebSocket):
    return None
