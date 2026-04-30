from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class MandiPrice(Base):
    __tablename__ = "mandi_prices"

    id = Column(Integer, primary_key=True, index=True)
    crop_name = Column(String, index=True)
    district = Column(String, index=True)
    price = Column(Integer)
    date = Column(Date)