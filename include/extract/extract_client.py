
import os
import requests as rq 
import pandas as pd 


class ExtractClient:
    def __init__(self):
         pass 
    
    def extract_client(self, ulr_endpoint):
         self.request = rq.get(ulr_endpoint)
         self.response = self.request.json() 
         df_client_raw = pd.DataFrame(self.response)

         return df_client_raw
    
    

     