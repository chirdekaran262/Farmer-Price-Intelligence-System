from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import MandiPrice
from sqlalchemy import func

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/prices")
def get_prices(crop: str, district: str, db: Session = Depends(get_db)):
    data = db.query(MandiPrice).filter(
        func.lower(MandiPrice.crop_name) == crop.lower(),
        func.lower(MandiPrice.district) == district.lower()
    ).all()

    result = []
    for row in data:
        result.append({
            "crop": row.crop_name,
            "district": row.district,
            "price": row.price,
            "date": row.date
        })

    return result