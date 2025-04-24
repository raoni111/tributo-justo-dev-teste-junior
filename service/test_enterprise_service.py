from fastapi import HTTPException
from model.enterprise import EnterpriseBaseModel
from service.enterprise_service import EnterpriseService
import uuid

default_enterprise = {
    "cnpj": str(uuid.uuid4().int)[:14],
    "corporate_reason": "Empresa Pythonic",
    "sector": "Veterinária",
    "opening_date": "2025-04-23"
}

enterprise_id = 0

def create_enterprise_model() -> EnterpriseBaseModel:
    enterprise_model = EnterpriseBaseModel(
        cnpj=default_enterprise["cnpj"],
        corporate_reason=default_enterprise["corporate_reason"],
        sector=default_enterprise["sector"],
        opening_date=default_enterprise["opening_date"]
    )
    
    return enterprise_model

def test_post_enterprise():
    global enterprise_id
    
    enterprise_model = create_enterprise_model()
    
    enterprise_service = EnterpriseService()
    
    enterprise_res = enterprise_service.post_enterprise(enterprise_model)
    
    assert enterprise_res["cnpj"] == default_enterprise["cnpj"]
    
    enterprise_id = enterprise_res["id"]
    
def test_post_existing_enterprise():
    enterprise_model = create_enterprise_model()
    
    enterprise_service = EnterpriseService()
    
    try:
        enterprise_res = enterprise_service.post_enterprise(enterprise_model)

        assert False, "Esperava um empresa repetida"
    except HTTPException as e:
        assert e.status_code == 409
        
        assert e.detail["statusCode"] == 409
        
    
def test_get_all_enterprise():
    enterprise_service = EnterpriseService()
    
    companies = enterprise_service.get_all_companies()
    
    assert len(companies) > 0
    
def test_get_enterprise_by_cnpj():
    enterprise_service = EnterpriseService()
    
    enterprise = enterprise_service.get_enterprise_by_CNPJ(default_enterprise["cnpj"])
    
    assert enterprise["cnpj"] == default_enterprise["cnpj"]
    
def test_get_companies_by_sector():
    enterprise_service = EnterpriseService()
    
    companies = enterprise_service.get_companies_by_sector(default_enterprise["sector"])
    
    assert len(companies) > 0
    
def test_delete_enterprise():
    enterprise_service = EnterpriseService()
    
    enterprise = enterprise_service.delete_enterprise(enterprise_id)
    
    assert enterprise["enterpriseId"] == enterprise_id