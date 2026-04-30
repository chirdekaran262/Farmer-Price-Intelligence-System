from fastapi import FastAPI
from app.routes import prices, recommendation, trend
from app.routes import recommendation
from app.routes import trend
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # or ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(prices.router)
app.include_router(recommendation.router)
app.include_router(trend.router)

@app.get("/")
def root():
    return {"message": "API running ??"}