""" Module providing excle file querying """
import pandas as pd

from excel_client.excel_client import ExcelClient
import ygo_client.constants as c

def query_excel_file(query_string: str) -> pd.DataFrame:
    """
    Queries an Excel file for rows where 'Name' matches the provided string.
    Args:
        query_string (str): The string to search for in the 'Name' column of the Excel sheet.
        Should be formatted for use in df.query(f'Name == "{query_string}"
    Returns:
        pandas.DataFrame: A DataFrame containing all rows that match the search string.
    """
    excel_client = ExcelClient()
    df = ExcelClient.load_excel(sheet_name=c.SHEET_NAME,
                                 header=True,
                                 return_output=True)
    query_results = df.query(f'Name == "{query_string}"')
    print(query_results)
