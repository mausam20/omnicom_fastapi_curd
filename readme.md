# Omnicom Crude Oil Import API

A FastAPI-based backend service for managing U.S. crude oil import data with PostgreSQL
---

## Features

- Perform CURD operations on crude oil import records
- while fetching filter records by origin country also has pagination support (`skip`, `limit`)
- Create new record, also can create in bulk
- Update and deleted records by ID
- Ingestion code to insert data from csv to Postgres

---

## Project Structure
```
omnicom_fastapi_curd/  
 ├── src/  
  ├── main.py  
  ├── api_routes.py  
  ├── config.json  
  ├── database.py  
  ├── test/  
  └── api_logic/  
   ├── controller.py  
   ├── database_layer.py  
   ├── params_schema.py  
   └── response_schemas.py  
 ├── readme.md  
 ├── requirments.txt  
 ├── ingest_data.py  
```

---

## Requirements

- Python 3.8+
- PostgreSQL running locally


---
## Database setup
- Create a database in Postgres 
- run ingest_data_pd.py script to create table and insert all the records from data.csv
- add the database cofigurations in .env file, which is used by src/database.py to make connection
- eg: 
```bash
DB_USER=postgres
DB_PASSWORD=root
DB_NAME=omnicom
DB_Host=localhost
DB_Port=5432
```

---
## Run the Application
- Create virtual environment
- Activate virtual environment
- Install the reqirements
- Run FastAPI Application
```bash
venv {enviromnet name}
./{enviromnet name}/Scripts/activate
enviromnet name}
cd src
uvicorn main:app --reload
```

- This will start your FastAPI application on port 8000 on localhost
- To access the swagger UI go to http://localhost:8000/doc  
![Swagger Image](imgs/Screenshot%202025-07-07%20202609.png)
  
  

- For In-depth understating of the APIs go to http://localhost:8000/redoc, it gives more clean, readable API reference
- ![redocs Image](imgs/Screenshot%202025-07-07%20203337.png)

---

## API usage (including request/response examples)

### GET /imports/ - Get Imports with Filters
- Example Request
```bash
curl -X 'GET' \
  'http://localhost:8000/imports/?country=Algeria&skip=0&limit=10' \
  -H 'accept: application/json'
```
- Response
```bash
[
  {
    "id": 2,
    "year": 2009,
    "month": 1,
    "origin_name": "usa",
    "origin_type_name": "Country",
    "destination_name": "CHEVRON USA INC / TX",
    "destination_type_name": "Refinery",
    "grade_name": "Light Sweet",
    "quantity": 850.0
  }
]

```
---

### POST /imports/ - Create an Import
- Example Request
```bash 
curl -X 'POST' \
  'http://localhost:8000/imports/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "year": 2006,
  "month": 0,
  "origin_name": "string",
  "origin_type_name": "string",
  "destination_name": "string",
  "destination_type_name": "string",
  "grade_name": "string",
  "quantity": 0
}'

```
Response

```bash
{
  "id": 483066,
  "year": 2006,
  "month": 0,
  "origin_name": "string",
  "origin_type_name": "string",
  "destination_name": "string",
  "destination_type_name": "string",
  "grade_name": "string",
  "quantity": 0
}
```
---

### PUT /imports/ - Update an Import
- Example Request
```bash
curl -X 'PUT' \
  'http://localhost:8000/imports/?id=483066' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "month": 5
}'
```
Response
```bash
{
  "id": 483066,
  "year": 2006,
  "month": 5,
  "origin_name": "string",
  "origin_type_name": "string",
  "destination_name": "string",
  "destination_type_name": "string",
  "grade_name": "string",
  "quantity": 0
}
```
---

### DELETE /imports/ - Delete an Import

- Example Request
```bash
curl -X 'DELETE' \
  'http://localhost:8000/imports/?id=483066' \
  -H 'accept: application/json'
```

Response
```bash
{
  "id": 483066,
  "detail": "Deleted"
}
```

---

### POST /imports/bulk - Create multiple Imports
- Example Request
```bash 
curl -X 'POST' \
  'http://localhost:8000/imports/bulk' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "records": [
    {
      "year": 0,
      "month": 0,
      "origin_name": "string",
      "origin_type_name": "string",
      "destination_name": "string",
      "destination_type_name": "string",
      "grade_name": "string",
      "quantity": 0
    }
  ]
}'
```

Response
```bash
{
  "message": "1 records inserted successfully."
}
```







