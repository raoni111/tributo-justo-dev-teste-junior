from fastapi import FastAPI
from routes.enterprise_routes import enterpriseRouter

app = FastAPI()

app.include_router(enterpriseRouter)