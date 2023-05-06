import openpyxl
import logging
logging.basicConfig(filename="my_logs.log", level=logging.DEBUG)
book = openpyxl.load_workbook("./data_pdf.xlsx")
data = book.active
pdf = './pdf/test.pdf'

slides = str(data[f"D{2}"].value).split(',')
slides = [f'Slide_{x}.jpg' for x in slides]
print('==================')
print(slides)
print('==================')
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")