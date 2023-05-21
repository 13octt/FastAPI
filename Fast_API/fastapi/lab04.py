from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Dashboard(BaseModel):
    device_name: str
    enabled: bool
    last_connection_time: int
    last_disconnection_time: int

class SensorData(BaseModel):
    temperature: int
    humidity: int
    light: int

class Log(BaseModel):
    device_name: str
    device_ip: str
    device_id: int
    value_name: str
    value: int
    received_time: int

class ApiResponse(BaseModel):
    error: bool
    message: str
    dashboard: Dashboard
    sensor_data: SensorData
    log: Log

@app.get("/api")
async def get_api():
    dashboard = Dashboard(
        device_name="Device 1",
        enabled=True,
        last_connection_time=1621664400,
        last_disconnection_time=1621664500
    )
    sensor_data = SensorData(
        temperature=25,
        humidity=50,
        light=100
    )
    log = Log(
        device_name="Device 1",
        device_ip="192.168.1.100",
        device_id=1,
        value_name="Value 1",
        value=10,
        received_time=1621664600
    )
    response = ApiResponse(
        error=True,
        message="This is a message of API",
        dashboard=dashboard,
        sensor_data=sensor_data,
        log=log
    )
    return response

@app.post("/api")
async def post_api(data: ApiResponse):
    # Do something with the received data
    return {"message": "Data received successfully"}
