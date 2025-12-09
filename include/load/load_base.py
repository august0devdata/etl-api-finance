import logging

logger = logging.getLogger(__name__)

class BaseLoad:
    def __init__(self, engine):
        self.engine = engine

    def load(self, dataframe, table_name):
        logger.info(f"informação carregada na tabela {table_name}")

        dataframe.to_sql(
            table_name,
            self.engine,
            if_exists="append",
            index=False
        )

        logger.info(f"Loaded {len(dataframe)} rows into {table_name}")
