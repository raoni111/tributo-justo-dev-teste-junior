from model.enterprise import EnterpriseBaseModel
import sqlite3
import os

class EnterpriseService:
    database_dir = os.path.join(os.path.dirname(__file__), '..', 'database', 'enterprise_db.sql')
    
    # função executa um query (SELECT) no banco de dados e retorna todas as empresas
    def get_all_companies(self):
        companies: list[EnterpriseBaseModel] = []
        
        with sqlite3.connect(self.database_dir) as conn:
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM enterprise")

            companies = cursor.fetchall()
            
        return companies