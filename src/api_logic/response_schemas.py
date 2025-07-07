from pydantic import BaseModel

class CrudeOilImportResponse(BaseModel):
    id: int
    year: int
    month: int
    origin_name: str
    origin_type_name: str
    destination_name: str
    destination_type_name: str
    grade_name: str
    quantity: float

    class Config:
        orm_mode = True

