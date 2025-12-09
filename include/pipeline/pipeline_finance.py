from dotenv import load_dotenv
import os
import logging

from include.extract.extract_account import ExtractAccount
from include.extract.extract_client import ExtractClient

from include.load.load_account import LoadAccount
from include.load.load_client import LoadClient

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)

load_dotenv()

def main():
    logging.info("Starting ETL pipeline...")

    URL_ENGINE = os.getenv("DATABASE_URL")
    API_ACCOUNT = os.getenv("API_END_CON")
    API_CLIENT = os.getenv("API_END_CLI")

    df_accounts = ExtractAccount().extract(API_ACCOUNT)
    df_clients  = ExtractClient().extract(API_CLIENT)


    LoadAccount(URL_ENGINE).load(df_accounts, "raw_account")
    LoadClient(URL_ENGINE).load(df_clients, "raw_cliente")

    logging.info("ETL pipeline finalizado com sucesso.")

if __name__ == "__main__":
    main()
