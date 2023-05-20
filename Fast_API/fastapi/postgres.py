from fastapi import FastAPI
import asyncpg
from pydantic import BaseModel
from datetime import datetime

async def connect_to_db():
    conn = await asyncpg.connect(
        user="duylam",
        password="123",
        database="data",
        host="your_host",
        port="your_port"
    )
    return conn

class SensorData(BaseModel):
    temperature: float
    humidity: float

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.state.db = await connect_to_db()

@app.on_event("shutdown")
async def shutdown():
    await app.state.db.close()

@app.post("/data")
async def save_sensor_data(sensor_data: SensorData):
    current_time = datetime.now()
    query = "INSERT INTO sensor_data (temperature, humidity, created_at) VALUES ($1, $2, $3)"
    await app.state.db.execute(query, sensor_data.temperature, sensor_data.humidity, current_time)
    return {"message": "Data saved successfully"}
