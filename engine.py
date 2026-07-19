# engine.py
from typing import Dict, List, Any

class EcoRouteEngine:
    def __init__(self):
        # Base emissions: grams of CO2 equivalents emitted per kilometer (gCO2e/km)
        self.emission_factors = {
            "electric_truck": 80.0,    # Baseline for EV trucks on an average grid
            "diesel_truck": 270.0,     # Standard heavy commercial diesel vehicle
            "cargo_rail": 25.0,        # Highly efficient mass transit per unit
            "delivery_drone": 15.0,    # Low payload, ultra-localized electric transit
            "cargo_ship": 12.0         # Highly efficient per kilometer for maritime legs
        }

    def calculate_carbon_footprint(self, distance: float, mode: str, grid_intensity: float) -> float:
        """
        Calculates total gCO2 emitted for a specific leg of a journey.
        Adjusts electric vehicles dynamically based on the local grid's fossil fuel reliance.
        """
        base_factor = self.emission_factors.get(mode, 200.0) # Default fallback if mode unknown
        
        # Dynamic Grid Regulation: If it relies on electricity, its footprint scales
        # with the regional grid's current carbon intensity index (100.0 is the baseline norm).
        if mode in ["electric_truck", "delivery_drone"]:
            grid_modifier = grid_intensity / 100.0
            adjusted_factor = base_factor * grid_modifier
            return distance * adjusted_factor
        
        return distance * base_factor

    def find_optimal_eco_route(self, routes: List[Dict[str, Any]], live_grid_intensity: float) -> Dict[str, Any]:
        """
        Parses multiple multi-modal route choices and isolated paths, returning 
        the absolute cleanest alternative alongside comprehensive data breakdown.
        """
        if not routes:
            return {"error": "No viable routes provided to analyze."}

        optimized_routes = []

        for route in routes:
            total_carbon = 0.0
            total_distance = 0.0
            leg_breakdowns = []

            for leg in route.get('legs', []):
                dist = leg.get('distance_km', 0.0)
                mode = leg.get('transport_mode', 'unknown')
                
                carbon_emitted = self.calculate_carbon_footprint(dist, mode, live_grid_intensity)
                
                total_carbon += carbon_emitted
                total_distance += dist
                
                leg_breakdowns.append({
                    "transport_mode": mode,
                    "distance_km": dist,
                    "carbon_gCO2": round(carbon_emitted, 2)
                })

            optimized_routes.append({
                "route_name": route.get("route_name", "Unnamed Route"),
                "total_distance_km": total_distance,
                "total_carbon_gCO2": round(total_carbon, 2),
                "legs": leg_breakdowns
            })

        # Sort routes ascending based on total carbon emissions
        optimized_routes.sort(key=lambda x: x["total_carbon_gCO2"])

        # Construct final bulletproof response metadata
        return {
            "eco_recommendation": optimized_routes[0],
            "all_evaluated_options": optimized_routes
        }
