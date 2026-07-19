# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from engine import EcoRouteEngine

# 1. Initialize API Framework and Core Engine
app = FastAPI(
    title="EcoRoute Core API",
    description="Visionary Open-Source Multi-Modal Carbon Routing Engine for Next-Gen Logistics.",
    version="1.0.0"
)
engine = EcoRouteEngine()

# 2. Define Strict Request Validation Schemas using Pydantic
class RouteLeg(BaseModel):
    transport_mode: str = Field(..., example="electric_truck", description="Modes: electric_truck, diesel_truck, cargo_rail, delivery_drone, cargo_ship")
    distance_km: float = Field(..., gt=0, example=45.5, description="Distance of travel segment in kilometers")

class RouteOption(BaseModel):
    route_name: str = Field(..., example="Alternative North Corridor")
    legs: List[RouteLeg]

class OptimizationPayload(BaseModel):
    grid_intensity: float = Field(100.0, ge=10, le=500, example=85.0, description="Current carbon intensity index of local power grid. 100 is baseline baseline.")
    routes: List[RouteOption]

# 3. Define the Core App Endpoints
@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "EcoRoute Core Engine is fully operational. Access API docs at /docs"
    }

@app.post("/api/v1/optimize")
def optimize_logistics(payload: OptimizationPayload):
    try:
        # Convert Pydantic structures safely to primitive dict arrays for the engine processing core
        routes_data = [route.dict() for route in payload.routes]
        result = engine.find_optimal_eco_route(routes_data, payload.grid_intensity)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Algorithmic execution error: {str(e)}")
