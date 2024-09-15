import pandas as pd

from excel_client.excel_client import ExcelClient
import ygo_client.constants as c

def query_excel_file(query_string: str) -> pd.DataFrame:
    excel_client = ExcelClient(c.OUTPUT_PATH)
    df = excel_client.load_excel(sheet_name=c.SHEET_NAME,
                                 header=True,
                                 return_output=True)
    query_results = df.query(f'Name == "{query_string}"')
    print(query_results)
