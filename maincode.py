import PySimpleGUI as sg
import validators as va
import pyshorteners

sg.theme('DarkAmber')
sg.set_options(font = ("Consolas", 10))

label1 = ""
layout = [  [sg.Text('Python URL shortener!!')],
            [sg.Text('Enter URL'), sg.InputText('',key='inputURL')],
            [sg.Text('Shortened URL will appear here.',key = 'label00'), sg.Text(label1, key = 'label01'), sg.Button('Copy')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('URL Shortener', layout, resizable = True)

def urlshort(url):
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(url)
    return short_url

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Ok':
        if va.url(values['inputURL']):
            label1 = urlshort(values['inputURL'])
            window['label00'].update("Shortened URL: ")
            window['label01'].update(label1)
        elif not va.url(values['inputURL']):
            window['label00'].update("Invalid URL!!")
    elif event == 'Copy':
        surl = window['label01'].get()
        window.TKroot.clipboard_append(surl)

window.close()
