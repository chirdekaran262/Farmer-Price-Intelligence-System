from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import SessionLocal
from app.models import MandiPrice
from app.services.recommendation_service import calculate_recommendation
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

 
    
    
    
@router.get("/recommendation")
def get_recommendation(crop: str, district: str, db: Session = Depends(get_db)):

    data = db.query(MandiPrice).filter(
        func.lower(MandiPrice.crop_name) == crop.lower(),
        func.lower(MandiPrice.district) == district.lower()
    ).all()

    if not data:
        return {"error": "No data found"}

    result = calculate_recommendation(data)

    return {
        "crop": crop,
        "district": district,
        **result
    }