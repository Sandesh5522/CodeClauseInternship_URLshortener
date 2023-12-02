import PySimpleGUI as sg
import urlshortener as us

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
label1 = ""
layout = [  [sg.Text('Python URL shortener!!')],
            [sg.Text('Enter URL'), sg.InputText('',key='inputURL')],
            [sg.Text('Shortened URL will appear here.',key = 'label00'), sg.Text(label1, key = 'label01'), sg.Button('Copy')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    # print('You entered ', values[0])
    elif event == 'Ok':
        label1 = us.urlshort(values['inputURL'])
        window['label00'].update("Shortened URL: ")
        window['label01'].update(label1)
    elif event == 'Copy':
        surl = window['label01'].get()
        window.TKroot.clipboard_append(surl)

window.close()
