import tkinter as tk
from tkinter import ttk
from descargar_playlistV3 import obtener_info_videos_lista_reproduccion
from mp3_downloaderV2 import descargar_audio

root = tk.Tk()
root.title('MP3 DOWNLOADER')
root.geometry('500x200')

pestanas = ttk.Notebook(root)

# Pestaña 1 -------------------------------------------------------------
pestana1 = ttk.Frame(pestanas)

pestanas.add(pestana1, text='Single MP3 Downloader')

single_url_frame = ttk.Frame(pestana1)
single_url_frame.pack(pady=20)

single_url_lbl = ttk.Label(single_url_frame, text='Song URL: ')
single_url_lbl.grid(row=0, column=0, padx=10,pady=20)

single_url_entry = ttk.Entry(single_url_frame, width=60)
single_url_entry.grid(row=0, column=1, padx=10, pady=20)

def single_url_btn_get():
    url = single_url_entry.get()
    print(url)
    descargar_audio(url)

single_url_btn = ttk.Button(single_url_frame, text='Descargar', command=single_url_btn_get)
single_url_btn.grid(row=1, column=1, sticky='e', padx=10)



# Pestaña 2 -------------------------------------------------------------
pestana2 = ttk.Frame(pestanas)

pestanas.add(pestana2, text='Playlist Downloader')

playlist_url_frame = ttk.Frame(pestana2)
playlist_url_frame.pack(pady=20)

playlist_url_lbl = ttk.Label(playlist_url_frame, text='Playlist URL: ')
playlist_url_lbl.grid(row=0, column=0, padx=10, pady=20)

playlist_url_entry = ttk.Entry(playlist_url_frame, width=60)
playlist_url_entry.grid(row=0, column=1, padx=10, pady=20)

def playlist_url_btn_get():
    url = playlist_url_entry.get()
    print(url)
    obtener_info_videos_lista_reproduccion(url)

playlist_url_btn = ttk.Button(playlist_url_frame, text='Descargar')
playlist_url_btn.grid(row=1, column=1, sticky='e', padx=10)

# -----------------------------------------------------------------------
pestanas.pack(expand=True, fill='both')
root.mainloop()
