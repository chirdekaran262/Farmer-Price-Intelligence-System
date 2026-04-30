import pandas as pd
from datetime import datetime
from app.database import SessionLocal
from app.models import MandiPrice

def load_data():
    db = SessionLocal()

    df = pd.read_csv("data/mandi_prices.csv")

    for _, row in df.iterrows():
        try:
            date_obj = pd.to_datetime(row['date'])

            record = MandiPrice(
                crop_name=row['crop'],
                district=row['district'],
                price=int(row['price']),
                date=date_obj
            )
            print("add record")
            db.add(record)

        except Exception as e:
            print(f"Error processing row: {row} -> {e}")

    db.commit()
    db.close()

    print("Data loaded successfully ?")

if __name__ == "__main__":
    load_data()