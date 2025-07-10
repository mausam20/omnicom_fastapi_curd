from fastapi import HTTPException
from typing import List
from sqlalchemy.orm import Session
from database import Base
from sqlalchemy import Column, Integer, String, Float
from .params_schema import CrudeOilImportCreate, BulkCrudeOilImporCreate

class CrudeOilImport(Base):
    __tablename__ = "crude_oil_imports"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer)
    month = Column(Integer)
    origin_name = Column(String)
    origin_type_name = Column(String)
    destination_name = Column(String)
    destination_type_name = Column(String)
    grade_name = Column(String)
    quantity = Column(Float)


class CrudeOilRepository:
    def fetch_imports(self, db: Session, country: str, skip: int, limit: int):
        query = db.query(CrudeOilImport)
        if country:
            query = query.filter(CrudeOilImport.origin_name == country)
        return query.offset(skip).limit(limit).all()

    def insert_import(self, db: Session, data: CrudeOilImportCreate):
        # existing = db.query(CrudeOilImport).filter(
        #     CrudeOilImport.year == data.year,
        #     CrudeOilImport.month == data.month,
        #     CrudeOilImport.origin_name == data.origin_name
        # ).first()
        # if existing:
        #     raise HTTPException(status_code=409, detail="Duplicate import entry detected.")
        new_record = CrudeOilImport(**data.dict())
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        return new_record
    
    def insert_bulk_import(self, db:Session, data: BulkCrudeOilImporCreate):
        try:
            data 
            objects = [CrudeOilImport(**item.dict()) for item in data]
            db.bulk_save_objects(objects)
            db.commit()
            return {"message": f"{len(objects)} records inserted successfully."}
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Error inserting records: {str(e)}")
    
    def get_import(self, db: Session, import_id: int):
        return db.query(CrudeOilImport).filter(CrudeOilImport.id == import_id).first()
    
    def update_import(self, db: Session, db_import: CrudeOilImport, data: CrudeOilImportCreate):
        for key, value in data.items():
            setattr(db_import, key, value)
        db.commit()
        db.refresh(db_import)
        return db_import
    
    def delete_import(self, db: Session, db_import: CrudeOilImport):
        db.delete(db_import)
        db.commit()
        return db_import
