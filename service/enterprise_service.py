from fastapi import HTTPException, status
from model.enterprise import EnterpriseBaseModel
import sqlite3
import os

class EnterpriseService:
    database_dir = os.path.join(os.path.dirname(__file__), '..', 'database', 'enterprise_db.sql')
    
    # função tenta (INSERT INTO) adicionando uma empresa no banco de dados, se surgir uma exceção IntegrityError retorna uma uma mensagem de erro
    def post_enterprise(self, enterprise: EnterpriseBaseModel) -> EnterpriseBaseModel | None:
        try:
            with sqlite3.connect(self.database_dir) as conn:
                cursor = conn.cursor()
                
                cursor.execute(
                    "INSERT INTO enterprise (cnpj, corporate_reason, sector, opening_date) VALUES(?, ?, ?, ?)", 
                    (enterprise.cnpj, enterprise.corporate_reason, enterprise.sector, enterprise.opening_date)
                )
        except sqlite3.IntegrityError:
               raise HTTPException(
                    status.HTTP_409_CONFLICT, 
                    {
                        "statusCode": status.HTTP_409_CONFLICT,
                        "message": "CNPJ ja esta cadastrada no banco de dados"
                    } 
                )

        return self.get_enterprise_by_CNPJ(enterprise.cnpj)
    
    # função executa uma query (SELECT) no banco de dados e retorna todas as empresas
    def get_all_companies(self) -> list[EnterpriseBaseModel]:
        companies: list[EnterpriseBaseModel] = []
        
        with sqlite3.connect(self.database_dir) as conn:
            conn.row_factory = sqlite3.Row
            
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM enterprise")

            rows = cursor.fetchall()
            
            companies = [dict(row) for row in rows]
        
        return companies
    
    # função executa uma query (SELECT WHERE) e retorna uma empresa pelo CNPJ
    def get_enterprise_by_CNPJ(self, CNPJ: str) -> EnterpriseBaseModel | None:
        enterprise: EnterpriseBaseModel | None = None
        
        with sqlite3.connect(self.database_dir) as conn:
            conn.row_factory = sqlite3.Row
            
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM enterprise WHERE cnpj = ?", (CNPJ,))
            
            enterprise = dict(cursor.fetchone())
            
        return enterprise
    
    # Função executa uma query (SELECT WHERE) e retorna empresas filtrada por setor
    def get_companies_by_sector(self, sector: str) -> list[EnterpriseBaseModel]:
        enterprise: list[EnterpriseBaseModel] = []
        
        with sqlite3.connect(self.database_dir) as conn:
            conn.row_factory = sqlite3.Row
            
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM enterprise WHERE sector = ?", (sector,))
            
            rows = cursor.fetchall()
            
            enterprise = [dict(row) for row in rows]
            
        return enterprise
        
            