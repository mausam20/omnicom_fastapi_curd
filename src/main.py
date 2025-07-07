
from fastapi import FastAPI
from api_routes import router

app = FastAPI(title="Omnicom Crude Oil Import API")
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Omnicom API"}
