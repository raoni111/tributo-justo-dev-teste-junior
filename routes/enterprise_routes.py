from model.enterprise import EnterpriseBaseModel
from service.enterprise_service import EnterpriseService
from fastapi import APIRouter

enterpriseRouter = APIRouter()

# Rota response: retornar todas as empresas do banco de dados
@enterpriseRouter.get("/enterprise", tags=["enterprise"])
async def get_companies():
    companies: list[EnterpriseBaseModel] = []
    
    enterprise_service = EnterpriseService()
    
    companies = enterprise_service.get_all_companies()
    
    return companies