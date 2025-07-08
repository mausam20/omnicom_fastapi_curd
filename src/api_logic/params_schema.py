from pydantic import BaseModel, Field, validator
from typing import Optional, List

class ImportFilterParams(BaseModel):
    country: Optional[str] = Field(None, description="Filter by country of origin")
    skip: int = Field(0, ge=0, description="Records to skip for pagination")
    limit: int = Field(10, gt=0, le=100, description="Number of records to return")

    @validator('country', pre=True)
    def normalize_country(cls, country):
        if country is None: # change v
            return country
        return country.strip().lower()

class CrudeOilImportCreate(BaseModel):
    year: int
    month: int
    origin_name: str
    origin_type_name: str
    destination_name: str
    destination_type_name: str
    grade_name: str
    quantity: float

    @validator('origin_name', pre=True)
    def normalize_origin_name(cls, origin_name):
        return origin_name.strip().lower()

class BulkCrudeOilImporCreate(BaseModel):
    records: List[CrudeOilImportCreate]

class CrudeOilImportGetRecordByID(BaseModel):
    id :int = Field(description="Import ID to fetch record")

class CrudeOilImportUpdate(BaseModel):
    year: Optional[int] = None
    month: Optional[int] = None
    origin_name: Optional[str] = None
    origin_type_name: Optional[str] = None
    destination_name: Optional[str] = None
    destination_type_name: Optional[str] = None
    grade_name: Optional[str] = None
    quantity: Optional[float] = None

