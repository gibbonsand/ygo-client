from openpyxl import load_workbook
import pandas as pd

wb = pd.read_excel(
    '/Users/andrewgibbons/Downloads/Book 5.xlsx',
    sheet_name = 'YGO',
    header=0,
    #names=['Name', 'Amoount', 'In decks', 'SD', 'SD in decks', 'In Draft', 'In Bulk', 'SD in bulk']
)


print(wb)
print(wb.columns)