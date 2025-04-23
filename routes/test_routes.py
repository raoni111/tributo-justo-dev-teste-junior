from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

default_enterprise = {
    "id": 4,
    "cnpj": "99999999999999999",
    "corporate_reason": "Empresa teste",
    "sector": "SetorTeste",
    "opening_date": "2010-05-12"
}

def test_get_all_enterprise():
    response = client.get('/enterprise')
        
    assert response.status_code == 200
    
def test_post_enterprise():
    response = client.post(
        "/enterprise",
        json=default_enterprise
    )
    
    if response.status_code == 409:
        response.status_code == 409
        return
    assert response.status_code == 200

def test_get_enterprise_by_cnpj():
    response = client.get(f"/enterprise/CNPJ/{default_enterprise['cnpj']}")

    assert response.status_code == 200

def test_get_enterprise_by_sector():
    response = client.get(f"/enterprise/sector/{default_enterprise['sector']}")
    
    assert response.status_code == 200
    
    