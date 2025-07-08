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
-- Create virtual environment
-- Activate virtual environment
-- Install the reqirements
-- Run FastAPI Applicatio
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





