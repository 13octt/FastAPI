from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import asyncpg

app = FastAPI()

class SensorData(BaseModel):
    temperature: float
    humidity: float
    light: float

class Time(BaseModel):
    time_connect: datetime.strftime("%Y-%m-%d %H:%M:%S")
    time_disconnect: datetime.strftime("%Y-%m-%d %H:%M:%S")
    status: str
class ApiResponse(BaseModel):
    error: bool
    message: str
    data: SensorData
    # current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.post("/data")
async def save_sensor_data(data: SensorData):
    response = ApiResponse(error=False, message="This is a message of API", data=data)
    return response
