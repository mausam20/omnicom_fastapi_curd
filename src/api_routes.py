from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from api_logic.controller import CrudeOilController
from api_logic.params_schema import CrudeOilImportCreate, ImportFilterParams, CrudeOilImportUpdate, CrudeOilImportGetRecordByID
from api_logic.response_schemas import CrudeOilImportResponse
from database import get_db

router = APIRouter(prefix="/imports", tags=["Crude Oil Imports"])
controller = CrudeOilController()

@router.get("/", response_model=list[CrudeOilImportResponse])
def list_imports(params: ImportFilterParams = Depends(), db: Session = Depends(get_db)):
    return controller.get_imports(db, params)

@router.post("/", response_model=CrudeOilImportResponse, status_code=201)
def create_import(data: CrudeOilImportCreate, response: Response, db: Session = Depends(get_db)):
    created = controller.create_import(db, data)
    response.headers["Location"] = f"/imports/{created.id}"
    return created


@router.put("/", response_model=CrudeOilImportUpdate)
def update_import(data: CrudeOilImportUpdate,update_id: CrudeOilImportGetRecordByID = Depends(), db: Session = Depends(get_db)):
    data = data.dict(exclude_unset=True) 
    return controller.update_import(db, update_id, data)

@router.delete("/")
def delete_import(update_id: CrudeOilImportGetRecordByID = Depends(), db: Session = Depends(get_db)):
    controller.delete_import(db, update_id)
    return {"id": update_id.id, "detail": "Deleted"}