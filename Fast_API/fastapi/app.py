from fastapi import FastAPI
from typing import Any
from pydantic import BaseModel

class SensorData(BaseModel):
    distance: float
    light: float

class ApiResponse(BaseModel):
    error: bool
    message: str
    data: SensorData

app = FastAPI()

@app.get("/api")
async def read_api():
    data = SensorData(distance=20, light=50)
    response = ApiResponse(error=False, message="This is a message of API", data=data)
    return response


@app.post("/api")
async def Data(sensor_data: SensorData):
    num_leds = 0

    if (sensor_data.distance < 30):
        if(sensor_data.light > 200):
            num_leds = 3
        elif(sensor_data.light > 50):
            num_leds = 2
        elif(sensor_data.light > 5):
            num_leds = 1
        else:
            num_leds = 0
    else: 
        num_leds = 0
    return {"num_leds": num_leds}
