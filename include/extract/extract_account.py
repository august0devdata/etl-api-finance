from dotenv import load_dotenv
import os
import requests as rq 
import pandas as pd 


class ExtractAccount:
    def __init__(self):
         pass 
    
    def extract_account(self, ulr_endpoint):
         self.request = rq.get(ulr_endpoint)
         self.response = self.request.json() 
         df_account_raw = pd.DataFrame(self.response)

         return df_account_raw

     