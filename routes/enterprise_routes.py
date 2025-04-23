from fastapi import APIRouter, HTTPException, status
from model.enterprise import EnterpriseBaseModel
from service.enterprise_service import EnterpriseService

enterpriseRouter = APIRouter()

# Rota response: retornar todas as empresas do banco de dados
@enterpriseRouter.get(
    "/enterprise", 
    tags=["Enterprise"], 
    name="Retorna todas empresas do banco de dados",
    description="Basicamente retorna todas empresas registradas no banco de dados"
)
async def get_companies():
    companies: list[EnterpriseBaseModel] = []
    
    enterprise_service = EnterpriseService()
    
    companies = enterprise_service.get_all_companies()
    
    # Retorna uma exceção caso nao encontre uma empresa 
    if len(companies) == 0:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            {
                "statusCode": status.HTTP_404_NOT_FOUND,
                "message": f"Nenhuma empresa encontrada!"
            }
        )
    
    return {
        "statusCode": status.HTTP_200_OK,
        "companies": companies
    }

# Route response: retorna uma empresa pelo CNPJ
@enterpriseRouter.get(
    "/enterprise/{enterprise_CNPJ}", 
    tags=["Enterprise"], 
    name="Retorna uma empresa pelo CNPJ",
    description="Filtra empresas registradas no banco de dados pelo CNPJ enviado pelo usuário. Se não encontrar uma empresa, retorna uma exceção"
)
async def get_enterprise_by_CNPJ(enterprise_CNPJ: str):
    
    enterprise: EnterpriseBaseModel = {}
    
    enterprise_service = EnterpriseService()
    
    enterprise = enterprise_service.get_enterprise_by_CNPJ(enterprise_CNPJ)
    
    # Retorna uma exceção caso nao encontre uma empresa com o CNPJ sugerido
    if not enterprise:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, 
            {
                "statusCode": status.HTTP_404_NOT_FOUND,
                "message": f"Não foi possível encontrar uma empresa com o CNPJ {enterprise_CNPJ}"
            }
        )
    
    return {
        "statusCode": status.HTTP_200_OK,
        "enterprise": enterprise
    }
    
# Router: registra as informações da empresa no banco de dados
@enterpriseRouter.post(
        "/enterprise",
        tags=["Enterprise"],
        name="Cria uma empresa no banco de dados",
        description="A rota recebe as informações do cliente, valida os dados utilizando o EnterpriseBaseModel e, se forem válidos, cria uma empresa no banco de dados."
    )
def post_enterprise(enterprise_info: EnterpriseBaseModel):
    enterprise_service = EnterpriseService()
    
    enterprise = enterprise_service.post_enterprise(enterprise_info)
    
    if not enterprise:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            {
                "statusCode": status.HTTP_404_NOT_FOUND,
                "message": "Não foi possível registrar empresa"
            }    
        )
    
    return {
        "statusCode": status.HTTP_200_OK,
        "message": "Empresa registrada com sucesso",
        "enterprise": enterprise
    }
    