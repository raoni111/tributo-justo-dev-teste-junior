from fastapi import APIRouter

enterpriseRouter = APIRouter()

@enterpriseRouter.get("/enterprise", tags=["enterprise"])
def get_companies():
    return {
        "teste": "teste"
    }