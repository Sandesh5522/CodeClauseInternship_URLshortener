import PySimpleGUI as sg
import urlshortener as us

sg.theme('DarkAmber')

label1 = ""
layout = [  [sg.Text('Python URL shortener!!')],
            [sg.Text('Enter URL'), sg.InputText('',key='inputURL')],
            [sg.Text('Shortened URL will appear here.',key = 'label00'), sg.Text(label1, key = 'label01'), sg.Button('Copy')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Ok':
        label1 = us.urlshort(values['inputURL'])
        window['label00'].update("Shortened URL: ")
        window['label01'].update(label1)
    elif event == 'Copy':
        surl = window['label01'].get()
        window.TKroot.clipboard_append(surl)

window.close()
