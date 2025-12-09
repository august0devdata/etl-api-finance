from sqlalchemy import create_engine
from include.load.load_base import BaseLoad

class LoadClient(BaseLoad):
    def __init__(self, url_engine):
        engine = create_engine(url_engine)
        super().__init__(engine)
