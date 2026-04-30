from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import SessionLocal
from app.models import MandiPrice

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/price-trend")
def get_price_trend(crop: str, district: str, db: Session = Depends(get_db)):

    data = db.query(MandiPrice).filter(
        func.lower(MandiPrice.crop_name) == crop.lower(),
        func.lower(MandiPrice.district) == district.lower()
    ).order_by(MandiPrice.date.asc()).all()

    if not data:
        return {"error": "No data found"}

    dates = []
    prices = []

    for row in data:
        dates.append(row.date.strftime("%Y-%m-%d"))
        prices.append(row.price)

    return {
        "crop": crop,
        "district": district,
        "dates": dates,
        "prices": prices
    }