from fastapi import FastAPI
import random

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
    return {
        "symbol": data.get("symbol", "UNKNOWN"),
        "prediction": random.choice(["BUY", "SELL", "HOLD"]),
        "confidence": round(random.uniform(60, 95), 2)
    }