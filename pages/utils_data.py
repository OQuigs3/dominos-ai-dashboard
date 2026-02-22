import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def seed_state(st):
    if "seeded" in st.session_state:
        return

    rng = np.random.default_rng(42)

    # Inventory
    inv = pd.DataFrame([
        {"item": "Mozzarella Cheese", "on_hand": 9, "reorder_point": 15, "lead_time_days": 2},
        {"item": "Gluten-Free Crust", "on_hand": 18, "reorder_point": 20, "lead_time_days": 3},
        {"item": "Pepperoni", "on_hand": 34, "reorder_point": 25, "lead_time_days": 2},
        {"item": "Dough (Regular)", "on_hand": 62, "reorder_point": 40, "lead_time_days": 1},
        {"item": "Tomato Sauce", "on_hand": 28, "reorder_point": 18, "lead_time_days": 2},
    ])

    # Drivers
    drivers = pd.DataFrame([
        {"driver": "Driver A", "status": "On Delivery", "eta_min": int(rng.integers(12, 35)), "late_risk": "Medium"},
        {"driver": "Driver B", "status": "At Store", "eta_min": 0, "late_risk": "Low"},
        {"driver": "Driver C", "status": "On Delivery", "eta_min": int(rng.integers(18, 45)), "late_risk": "High"},
        {"driver": "Driver D", "status": "On Delivery", "eta_min": int(rng.integers(10, 30)), "late_risk": "Low"},
    ])

    # Orders
    now = datetime.now()
    orders = []
    for i in range(18):
        created = now - timedelta(minutes=int(rng.integers(0, 55)))
        status = rng.choice(["Queued", "In Oven", "Ready", "Out for Delivery"], p=[0.35, 0.25, 0.15, 0.25])
        eta = int(rng.integers(15, 45))
        orders.append({
            "order_id": f"DM-{1000+i}",
            "channel": rng.choice(["Web", "App", "Phone", "In-Store"], p=[0.35, 0.45, 0.15, 0.05]),
            "type": rng.choice(["Delivery", "Pickup"], p=[0.7, 0.3]),
            "status": status,
            "created_min_ago": int((now - created).total_seconds() / 60),
            "eta_min": eta,
            "notes": rng.choice(["", "GF request", "Extra sauce", "No-contact"], p=[0.55, 0.15, 0.15, 0.15]),
        })
    orders_df = pd.DataFrame(orders)

    # Busy-time forecast (next 12 hours)
    hours = pd.date_range(now.replace(minute=0, second=0, microsecond=0), periods=12, freq="H")
    base = np.array([12, 10, 9, 11, 14, 18, 24, 30, 28, 20, 16, 13])
    noise = rng.normal(0, 1.5, size=len(base))
    predicted_orders = np.maximum(0, base + noise).round(0).astype(int)
    forecast = pd.DataFrame({"hour": hours, "predicted_orders": predicted_orders})

    # Save to session state
    st.session_state["inventory"] = inv
    st.session_state["drivers"] = drivers
    st.session_state["orders"] = orders_df
    st.session_state["forecast"] = forecast

    # Chat messages
    st.session_state["messages"] = [
        {"role": "customer", "content": "What are your gluten-free options?"},
        {"role": "ai", "content": "We offer gluten-free crust in sizes up to medium."},
    ]

    st.session_state["seeded"] = True

def staffing_recommendation(orders_df, forecast_df):
    peak = int(forecast_df["predicted_orders"].max())
    queue = int((orders_df["status"] == "Queued").sum())
    out_for_delivery = int((orders_df["status"] == "Out for Delivery").sum())

    base = max(0, round(peak / 10) - 1)
    adjustment = 1 if (queue + out_for_delivery) >= 10 else 0
    add_drivers = max(0, base + adjustment)

    return {
        "peak_predicted_orders": peak,
        "queued": queue,
        "out_for_delivery": out_for_delivery,
        "suggested_additional_drivers": add_drivers,
    }
