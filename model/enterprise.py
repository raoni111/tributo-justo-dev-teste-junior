from pydantic import BaseModel

class EnterpriseBaseModel(BaseModel):
    id: int
    cnpj: str
    corporate_reason: str
    sector: str
    opening_date: str
    
    