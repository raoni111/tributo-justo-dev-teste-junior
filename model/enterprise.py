from pydantic import BaseModel, field_validator
from dateutil.parser import parse
from typing import Optional

class EnterpriseBaseModel(BaseModel):
    id: Optional[int] = None
    cnpj: str
    corporate_reason: str
    sector: str
    opening_date: str   
    
    @field_validator("cnpj")
    def cnpj_is_valid(cls, v):
        if (len(v) < 7):
            raise ValueError(f"CNPJ e invalido!")
        
        return v
        
    @field_validator("corporate_reason", "sector", "opening_date")
    def item_not_empty(cls, v):
        if (len(v) == 0):
            raise ValueError(f"O campo esta vazio {v}")
        
        return v
    