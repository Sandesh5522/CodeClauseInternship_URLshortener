import PySimpleGUI as sg
import urlshortener as us

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
label1 = "Shortened URL will appear here."
layout = [  [sg.Text('Python URL shortener!!')],
            [sg.Text('Enter URL'), sg.InputText('',key='inputURL')],
            [sg.Text(label1, key='label01')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    # print('You entered ', values[0])
    label1 = us.urlshort(values['inputURL'])
    window['label01'].update("Shortened URL: "+label1)

window.close()
