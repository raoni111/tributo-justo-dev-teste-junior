from model.enterprise import EnterpriseBaseModel
import sqlite3
import os

class EnterpriseService:
    database_dir = os.path.join(os.path.dirname(__file__), '..', 'database', 'enterprise_db.sql')
    
    # função executa uma query (SELECT) no banco de dados e retorna todas as empresas
    def get_all_companies(self) -> list[EnterpriseBaseModel]:
        companies: list[EnterpriseBaseModel] = []
        
        with sqlite3.connect(self.database_dir) as conn:
            conn.row_factory = sqlite3.Row
            
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM enterprise")

            companies = cursor.fetchall()
        
        return companies
    
    # função executa uma query (SELECT WHERE) e retorna uma empresa pelo cnpj
    def get_enterprise_by_cnpj(self, cnpj: str) -> EnterpriseBaseModel | None:
        enterprise: EnterpriseBaseModel | None = None
        
        with sqlite3.connect(self.database_dir) as conn:
            conn.row_factory = sqlite3.Row
            
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM enterprise WHERE cnpj = ?", (cnpj,))
            
            enterprise = cursor.fetchone()
            
        return enterprise
            