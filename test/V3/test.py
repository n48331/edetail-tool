import openpyxl
book = openpyxl.load_workbook("./data_pdf.xlsx")
data = book.active
pdf = './pdf/test.pdf'

slides = str(data[f"D{2}"].value).split(',')
slides = [f'Slide_{x}.jpg' for x in slides]
print('==================')
print(slides)
print('==================')
