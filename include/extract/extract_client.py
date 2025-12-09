from include.extract.extract_base import BaseExtract

class ExtractClient(BaseExtract):
    def extract(self, url):
        data = self.get_json(url)
        df = self.to_dataframe(data)
        return df
