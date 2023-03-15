import PySimpleGUI as sg

feet = sg.Text("Enter feet:")
feet_input = sg.Input()
inches = sg.Text("Enter inches:")
inches_input = sg.Input()
convert_button = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[feet, feet_input],
                                        [inches, inches_input],
                                        [convert_button]])

window.read()
window.close()
