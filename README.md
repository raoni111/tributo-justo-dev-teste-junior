# Desafio Tributo Justo

Desafio feito por `Raoni oliveira quevedo`

## inicialização

1. Inicie o gerenciador de dependência `(venv)`:
    ```powershell
       python.exe -m venv .venv
    ```

2. Inicia o venv `script/active` no terminal:
    ```powershell
       .\.venv\Scripts\activate 
    ```

3. Instale as dependências usando o comando a baixo: 
    ```powershell
       pip install -r requirement.txt
    ```

4. Iniciar projeto em `development`:
    ```powershell
       fastapi dev main.py
    ```

# Banco de Dados
se o arquivo ` enterprise_db ` não estiver em ` ./database/enterprise_db.sql `, crie o arquivo depois use o schema a baixo para criar a tabela ` enterprise ` 

```SQL
   CREATE TABLE enterprise (
	   id INTEGER PRIMARY KEY AUTOINCREMENT,
	   cnpj TEXT,
	   corporate_reason TEXT,
	   sector TEXT,
	   opening_date TEXT,
	   CONSTRAINT enterprise_UN UNIQUE (cnpj)
   );
```

# Rotas


## **[POST]**  `{api_url}/enterprise`

Rota recebe as informações da empresa do client e registra no banco de dados

### Informações envida via body 
```python
   {
      "cnpj": str,
      "corporate_reason": str,
      "sector": str,
      "opening_date":str
   }
```


### Response: <span style="color:green;">200 OK</span>

```python
   {
      "statusCode": 200,
      "message": "Empresa registrada com sucesso",
      "enterprise": {
         "id": int,
         "cnpj": str,
         "corporate_reason": str,
         "sector": str,
         "opening_date": str
      }
   }
```

## **[GET]**  `{api_url}/enterprise`
Rota retorna todas as empresas registradas no banco de dados

### Response: <span style="color:green;">200 OK</span>
```python
   {
      "statusCode": 200,
      "companies": [
         {
            "id": int,
            "cnpj": str,
            "corporate_reason": str,
            "sector": str,
            "opening_date": str
         },
         ...
      ]
   }
```

## **[GET]**  `{api_url}/enterprise/CNPJ/{enterprise_CNPJ}`
Rota busca uma empresa especifica pelo ` CNPJ ` enviado por parâmetro pelo client

### Response: <span style="color:green;">200 OK</span>
```python
   {
      "statusCode": 200,
      "enterprise": {
         "id": int,
         "cnpj": str,
         "corporate_reason": str,
         "sector": str,
         "opening_date": str
      }
   }
```

## **[GET]**  `{api_url}/enterprise/sector/{enterprise_sector}`
Rota busca empresas relacionada com o `setor` enviador por parâmetro pelo client

### Response: <span style="color:green;">200 OK</span>
```python
   {
      "statusCode": 200,
      "companies": [
         {
            "id": 4,
            "cnpj": "12345678000199",
            "corporate_reason": "Empresa Alpha Ltda",
            "sector": "Comércio",
            "opening_date": "2010-05-12"
         }
      ]
   }  
```