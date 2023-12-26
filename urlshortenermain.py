import PySimpleGUI as sg
import validators as va
import pyshorteners
import sys

# This bit gets the taskbar icon working properly in Windows.
if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'CompanyName.ProductName.SubProduct.VersionInformation') # Arbitrary string

sg.theme('DarkAmber')
sg.set_options(font = ("Bahnschrift", 10), margins=(5,5,5,5), \
               auto_size_buttons=True, auto_size_text=True)

label1 = ""
layout = [  [sg.Text('Python URL shortener!!')],
            [sg.Text('Enter URL'), sg.InputText('',key='inputURL')],
            [sg.Text('Shortened URL will appear here.',key = 'label00'), \
             sg.Text(label1, key = 'label01'), sg.Button('Copy')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('URL Shortener', layout, resizable = True, icon='icons8_shorten_urls.ico')

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
        window['Copy'].update('Copied!')

window.close()
