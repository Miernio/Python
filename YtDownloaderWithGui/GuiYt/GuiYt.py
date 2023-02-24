import PySimpleGUI as sg
from pytube import YouTube
import os

sg.theme('DarkAmber')
layout = [[sg.Text('Witam w programie do pobierania muzyki i filmow!')],
          [sg.Text('Wprowadz link YT'), sg.InputText()],
          [sg.Text('Prosze podac link', text_color="red", key="_link_", visible=False)],
          [sg.Text('Wprowadz sciezke docelowa'), sg.InputText(), sg.FolderBrowse()],
          [sg.Text('Prosze podac sciezke', text_color="red", key="_sciezka_", visible=False)],
          [sg.Radio('MP3', 'grp1'), sg.Radio('MP4', 'grp1')],
          [sg.Text('Prosze podac typ pliku', text_color="red", key="_typ_", visible=False)],
          [sg.Text('Wystapil nieoczekiwany blad sprawdz podane dane', text_color="red", key="_err2_", visible=False)],
          [sg.Text('Pomyslnie pobrano ', text_color="green", key="_pobrano_", visible=False)],
          [sg.Button('Download'), sg.Button('EXIT')]]
window = sg.Window('YT-downloader', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    if event == 'Download':
        window['_link_'].Update(visible=False)
        window['_pobrano_'].Update(visible=False)
        window['_sciezka_'].Update(visible=False)
        window['_typ_'].Update(visible=False)
        window['_err2_'].Update(visible=False)
        window.refresh()
        if values[0] != '': 
            link = values[0]
            try:
                yt = YouTube(link)
            except:
                window['_err2_'].Update(visible=True)
            if values[2] == False and values[3] == False:
                window['_typ_'].Update(visible=True)
            else:
                if values[2] == False:
                    try:
                        yt = yt.streams.get_highest_resolution()
                        if values[1] != '':
                            plik = yt.download(output_path=values[1])
                            if os.path.isfile(plik):
                                window['_pobrano_'].Update('Pomyslnie pobrano ' + yt.title, visible=True)
                        else:
                            window['_sciezka_'].Update(visible=True)
                    except:
                        window['_err2_'].Update(visible=True)
                else:
                    try:
                        yt = yt.streams.filter(only_audio=True).first()
                        if values[1] != '':
                            plik = yt.download(output_path=values[1])
                            base, ext = os.path.splitext(plik)
                            new_file = base + '.mp3'
                            os.rename(plik, new_file)
                            if os.path.isfile(new_file):
                                window['_pobrano_'].Update('Pomyslnie pobrano ' + yt.title, visible=True)
                        else:
                            window['_sciezka_'].Update(visible=True)
                    except:
                        window['_err2_'].Update(visible=True)

        else:
            window['_link_'].Update(visible=True)

window.close()
