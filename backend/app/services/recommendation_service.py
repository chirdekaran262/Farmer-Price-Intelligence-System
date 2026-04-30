from typing import List
from app.models import MandiPrice


def calculate_recommendation(data: List[MandiPrice]):

    if not data:
        return None

    # Sort latest first
    data = sorted(data, key=lambda x: x.date, reverse=True)

    current_price = data[0].price

    prices = [row.price for row in data]

    # Short-term trend (last 3)
    short_window = prices[:3] if len(prices) >= 3 else prices

    # Long-term trend (last 7)
    long_window = prices[:7] if len(prices) >= 7 else prices

    short_avg = sum(short_window) / len(short_window)
    long_avg = sum(long_window) / len(long_window)

    # Prediction logic
    if short_avg > long_avg:
        predicted_price = short_avg  # upward trend
    else:
        predicted_price = short_avg  # downward or stable

    # Decision logic
    if current_price > long_avg and predicted_price < current_price:
        recommendation = "SELL"
    elif predicted_price > current_price:
        recommendation = "WAIT"
    else:
        recommendation = "HOLD"

    return {
        "current_price": current_price,
        "short_avg": round(short_avg, 2),
        "long_avg": round(long_avg, 2),
        "predicted_price": round(predicted_price, 2),
        "recommendation": recommendation
    }