import PySimpleGUI as sg
from convertor import converter



feet = sg.Text('Enter feet:')
feet_in = sg.In(key='feet')
inches = sg.Text('Enter inches')
inches_in = sg.In(key='inches')
convert = sg.B("Convert")
output = sg.T('', key='output')

window = sg.Window("Convertor", layout=[[feet, feet_in],
                                        [inches, inches_in],
                                        [convert, output]])

while True:
    event, values = window.read()
    feet = float(values['feet'])
    inches = float(values['inches'])

    result = converter(feet, inches)
    window['output'].update(value=f"{result} m", text_color='Blue')
    match event:
        case sg.WIN_CLOSED:
            break
window.close()