import PySimpleGUI as sg

layout = [
    [sg.Text('Enter your Name: '), sg.InputText()],
    [sg.Text('Enter your age:'), sg.InputText()],
    [sg.Text('Enter your height:'), sg.InputText()],
    [sg.Text('Enter your weight:'), sg.InputText()],
    [sg.OK(), sg.Cancel()]
]

window = sg.Window('BMI CALCULATOR', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()
