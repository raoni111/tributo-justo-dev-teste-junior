from typing import Annotated
from fastapi import APIRouter, HTTPException, Query
from model.enterprise import EnterpriseBaseModel
from service.enterprise_service import EnterpriseService

enterpriseRouter = APIRouter()

# Rota response: retornar todas as empresas do banco de dados
@enterpriseRouter.get("/enterprise", tags=["Enterprise"])
async def get_companies():
    companies: list[EnterpriseBaseModel] = []
    
    enterprise_service = EnterpriseService()
    
    companies = enterprise_service.get_all_companies()
    
    return companies

# Route response: retorna uma empresa pelo cnpj
@enterpriseRouter.get("/enterprise/{enterprise_cnpj}", tags=["Enterprise"], name="Retorna uma empresa pelo cpnj")
async def get_enterprise_by_cnpj(enterprise_cnpj: str):
    
    enterprise: EnterpriseBaseModel = {}
    
    enterprise_service = EnterpriseService()
    
    enterprise = enterprise_service.get_enterprise_by_cnpj(enterprise_cnpj)
    
    # Retorna uma exceção caso nao encontre uma empresa com o cnpj sugerido
    if not enterprise:
        raise HTTPException(
            404, 
            {
                "statusCode": 400,
                "message": f"Não foi possível encontrar uma empresa com o cnpj {enterprise_cnpj}"
            }
        )
    
    return enterprise