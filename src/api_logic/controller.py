from fastapi import HTTPException
from sqlalchemy.orm import Session
from .database_layer import CrudeOilRepository
from .params_schema import CrudeOilImportCreate, ImportFilterParams, CrudeOilImportUpdate, CrudeOilImportGetRecordByID, BulkCrudeOilImporCreate

class CrudeOilController:
    def __init__(self):
        self.repo = CrudeOilRepository()

    def get_imports(self, db: Session, params: ImportFilterParams):
        return self.repo.fetch_imports(db, country=params.country, skip=params.skip, limit=params.limit)

    def create_import(self, db: Session, data: CrudeOilImportCreate):
        return self.repo.insert_import(db, data)
    
    def bulk_insert(self,db: Session, data: BulkCrudeOilImporCreate):
        return self.repo.insert_bulk_import(db, data)
        
    def update_import(self, db: Session, update_id: CrudeOilImportGetRecordByID, data: CrudeOilImportUpdate):
        db_import = self.repo.get_import(db, update_id.id) 
        if db_import:
            return self.repo.update_import(db, db_import, data)
        raise HTTPException(status_code=404, detail=f"no record found with id={update_id.id}")
            

    def delete_import(self, db: Session, update_id: CrudeOilImportGetRecordByID):
        db_import = self.repo.get_import(db, update_id.id)
        if db_import:
            return self.repo.delete_import(db, db_import)
        raise HTTPException(status_code=404, detail=f"no record found with id={update_id.id}")
