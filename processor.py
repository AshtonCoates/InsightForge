import openai
import pandas as pd
from typing import IO

class QueryProcesser:

    def __init__(self, codes:str, data:IO) -> None:
        self.codes = codes
        self.data = data
        self.df = self.data_to_df()

    def data_to_df(self) -> pd.DataFrame:
        if self.data.endswith('.csv'):
            return pd.read_csv(self.data)
        elif self.data.endswith('.xls') or self.data.endswith('.xlsx'):
            return pd.read_excel(self.data)
        else:
            raise ValueError("Unsupported file format")
        
