import requests
import pandas as pd
import logging
from requests.adapters import HTTPAdapter, Retry

logger = logging.getLogger(__name__)

class BaseExtract:
    def __init__(self):
        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=1)
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

    def get_json(self, url):
        logger.info(f"Realizando requisição para: {url}")
        response = self.session.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    def to_dataframe(self, data):
        df = pd.DataFrame(data)
        if df.empty:
            logger.warning("Informação vazia!")
        return df
