from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)

default_enterprise = {
    "cnpj": str(uuid.uuid4().int)[:14],
    "corporate_reason": "Empresa Pythonic",
    "sector": "Veterinária",
    "opening_date": "2025-04-23"
}

enterprise_id = 0

def test_get_all_enterprise():
    response = client.get('/enterprise')
        
    assert response.status_code in [200, 404]
    
def test_post_enterprise():
    global enterprise_id
    
    response = client.post(
        "/enterprise",
        json=default_enterprise
    )
    
    enterprise_res = response.json()
    

    assert response.status_code == 200
    
    if response.status_code == 409:
        return
    
    assert enterprise_res["enterprise"]["cnpj"] == default_enterprise["cnpj"]
    
    enterprise_id = enterprise_res["enterprise"]["id"]

def test_post_existing_enterprise():
    response = client.post(
        "/enterprise",
        json=default_enterprise
    )
    
    assert response.status_code == 409

def test_get_enterprise_by_CNPJ():
    response = client.get(f"/enterprise/CNPJ/{default_enterprise['cnpj']}")

    assert response.status_code == 200

def test_get_enterprise_by_sector():
    response = client.get(f"/enterprise/sector/{default_enterprise['sector']}")
    
    assert response.status_code == 200
    
def test_delete_enterprise():

    response = client.delete(f"/enterprise/{enterprise_id}")
    
    assert response.status_code == 200
    
    check_enterprise = client.get(f"/enterprise/CNPJ/{default_enterprise['cnpj']}")
    
    assert check_enterprise.status_code == 404