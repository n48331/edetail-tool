import openpyxl


def goToButton(x=1):
    goToButtons = ''
    for i in range(x):
        goToButtons += f'<div class="gotoBtn{i+1} goToButton" data-slide="s" data-flow="f0" data-info=""></div>\n'
    return goToButtons


def goToHomeButton(x=1):
    goToHomeButtons = ''
    for i in range(x):
        goToHomeButtons += f'<div class="Btn{i+1} goToHomeButton" data-flow="f0" data-slide="s" sub_slide=""></div>\n'
    return goToHomeButtons


def gotoSubParent():
    return '<div class="close" onclick="app.gotoSubParent()"></div>\n'

def carousalBtn(x):
    carousalBtns = ''
    for i in range(x):
        goToHomeButtons += f'<div class="slideBtn{i+1}" data-target="#carousel-example-generic" data-slide-to="{i+1}"></div>\n'
    return goToHomeButtons

book = openpyxl.load_workbook("./data.xlsx")
data = book.active

buttons = (data['E2'].value).split(',')
for button in buttons:
    print(eval(button))
    


# goToHomeButton()
