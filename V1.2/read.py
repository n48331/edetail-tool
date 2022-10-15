import openpyxl
book = openpyxl.load_workbook("./data.xlsx")
data = book.active

x = type(data['D2'].value)

print(x)
