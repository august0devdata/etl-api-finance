from dotenv import load_dotenv
import os 

from sqlalchemy import create_engine
import pandas as pd 

from include.extract.extract_account import ExtractAccount


load_dotenv() 

class LoadAccount:
    def __init__(self, url_engine):
        if url_engine is None:
            raise ValueError("URL não encontrada")
        self.engine = create_engine(url_engine)
    
    def load(self, dataframe_raw, table_name):
        dataframe_raw.to_sql(
            table_name,
            self.engine,
            if_exists="append",
            index=False
        )


if __name__ == "__main__":
    
    API_ACCOUNT = os.getenv("API_END_CON") 
    URL_ENGINE = os.getenv("DATABASE_URL")  

 
    extractor_account = ExtractAccount()
    tb_account_raw = extractor_account.extract_account(API_ACCOUNT) 

    load_account = LoadAccount(URL_ENGINE)
    load_account.load(tb_account_raw, 'raw_account')
