from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, Farm
from app.weather import get_weather

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/farms")
def create_farm(name:str, location:str, size:int, db:Session = Depends(get_db)):
    new_farm = Farm(name=name, location=location, size=size)
    db.add(new_farm)
    db.commit()
    db.refresh(new_farm)
    return {"message": "New farm added with sucsess", "data": new_farm}


@router.get("/farms")
def list_farms(db:Session = Depends(get_db)):
    farms = db.query(Farm).all()
    return {"farms": farms}


@router.get("/climate/{farm_id}")
def climate_farm(farm_id:int, db:Session = Depends(get_db)):
    farm = db.query(Farm).filter(Farm.id == farm_id).first()
    
    if not farm:
        raise HTTPException(status_code=404, detail="Fazenda não encontrada")
    
    climate_data = get_weather(farm.location)
    return {"farm": farm.name, "weather": climate_data}