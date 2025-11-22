from dotenv import load_dotenv
import os 

from sqlalchemy import create_engine
import pandas as pd 

from include.extract.extract_client import ExtractClient


load_dotenv() 

class LoadClient:
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
    
    API_CLIENT = os.getenv("API_END_CLI") 
    URL_ENGINE = os.getenv("DATABASE_URL")  

 
    extractor_client = ExtractClient() 
    tb_client_raw = extractor_client.extract_client(API_CLIENT) 

    load_client = LoadClient(URL_ENGINE)
    load_client.load(tb_client_raw, 'raw_cliente')
