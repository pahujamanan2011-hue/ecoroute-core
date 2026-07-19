# EcoRoute Core 🌍✈️🚛

EcoRoute Core is an open-source, AI-driven routing and carbon-accounting engine designed for the future of sustainable logistics. As global regulations tighten around carbon emissions, standard "fastest-route" mapping APIs are no longer sufficient. EcoRoute calculates the absolute greenest path by analyzing real-time power grid intensity, multi-modal vehicle efficiencies, and transit variables.

---

## 🚀 The Vision

Our goal is to provide developers, enterprise businesses, and supply chain managers with a plug-and-play API capable of instantly reducing logistics-based carbon footprints. By decoupling route planning from purely time-based metrics and shifting toward environmental metrics, EcoRoute helps prepare industries for mandatory carbon credit and penalty frameworks.

### Key Features
* **Multi-Modal Optimization:** Evaluates and splits routes across cargo rail, electric vehicles, diesel transport, and delivery drones.
* **Grid-Aware Routing:** Calculates dynamic EV carbon impact by measuring the real-time energy mix (solar/wind vs. coal) of local charging grids.
* **Developer-First API:** High-performance core built on Python and FastAPI, designed to integrate seamlessly into existing Fleet Management Systems (FMS).

---

## 🛠️ Architecture Overview



```
[Client Application / ERP]
│
▼ (FastAPI REST Endpoint)
[EcoRoute Core Engine]
│
┌─────────┴─────────┐
▼                   ▼
[Spatial Routing]    [AI Carbon Optimization] ──► [Live Grid & Weather Data]
```

---

## ⚡ Quick Start

### Prerequisites
* Python 3.10+
* Pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ecoroute-core.git](https://github.com/YOUR_USERNAME/ecoroute-core.git)
   cd ecoroute-core

```
 2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
   ```
 3. Run the live API server:
   ```bash
   uvicorn main:app --reload
   
   ```
   The local API will now be interactive and live at http://127.0.0.1:8000/docs
