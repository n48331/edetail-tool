import openpyxl

book = openpyxl.load_workbook("./data.xlsx")
data = book.active
