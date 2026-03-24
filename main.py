from fastapi import FastAPI
import yfinance as yf
import numpy as np

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DEMO AI Trading API is Live 🚀"}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "models_ready": True,
        "markets_loaded": ["indian_stocks", "us_stocks", "forex", "bullion"],
        "device": "cpu"
    }

@app.post("/predict")
def predict(data: dict):
    symbol = data.get("symbol", "RELIANCE.NS")

    try:
        df = yf.download(symbol, period="5d", interval="1h")

        if df.empty:
            return {"error": "No data found"}

        close_prices = df["Close"].values

        trend = close_prices[-1] - close_prices[0]

        if trend > 0:
            prediction = "BUY"
        elif trend < 0:
            prediction = "SELL"
        else:
            prediction = "HOLD"

        confidence = float(abs(trend) / close_prices[0] * 100)

        return {
            "symbol": symbol,
            "prediction": prediction,
            "confidence": round(min(confidence, 95), 2)
        }

    except Exception as e:
        return {"error": str(e)}
