"""APP
FastAPI app definition, initialization and definition of routes
"""

# # Installed # #
from imp import reload
from dotenv import load_dotenv
# from Slr import Prediction
from fastapi import FastAPI, WebSocket
from gesDec_api.routers import model,feedback
from gesDec_api.db import init_db

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000/",
]

# # Package # #
from gesDec_api.settings import api_settings 

load_dotenv()
init_db()

app = FastAPI(
    tags=['Model'],
    title="Gesture-Detection api"
)

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     prediction=Prediction()
#     while True:
#         data = await websocket.receive_json()
#         res=prediction.predict(data["keypoints"])
#         if(res!=None):
#             print(res)
#             await websocket.send_json(res)
#         # print(base64.b64decode(data))
#         # print("hi")
       

app.include_router(model.router)
app.include_router(feedback.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# def run():
#     """Run the API using Uvicorn"""
#     uvicorn.run(
#         'app:app',
#         port=api_settings.port,
#         host=api_settings.host,
#         reload=True,
#     )

if __name__=="__main__":
    print("running")
    # run()
    # uvicorn.run('app:app', host='localhost', port=8000,reload=True)
