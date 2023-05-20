from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Data(BaseModel):
    temperature: float
    humidity: float
    light: float

class Device(BaseModel):
    name: str
    connected: bool
    last_connected: datetime = None
    last_disconnected: datetime = None

class ApiResponse(BaseModel):
    error: bool
    message: str
    data: Data
    devices: Device

sensor_data = Data(temperature=0.0, humidity=0.0, light=0.0)
device = Device(name="My Device", connected=False)
api = ApiResponse(error=False, message="This is a message of API", data=sensor_data, devices=device)

@app.post("/lab04")
async def API(info:ApiResponse):
    # response = ApiResponse(error=False, message="This is a message of API", data=info.data, devices=info.devices)
    global api
    response = api
    return response
