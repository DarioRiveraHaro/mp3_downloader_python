import os
from pytube import YouTube

def descargar_audio(url):
    try:
        yt = YouTube(url)
        nombre_video = yt.title
        if nombre_existe('nombre_videos.txt', nombre_video):
            print(f'El audio "{nombre_video}" ya fue descargado. Saltando descarga...')
            return

        with open('nombre_videos.txt', 'a') as archivo:
            archivo.write(f'{nombre_video}\n')

        stream = yt.streams.filter(only_audio=True).first()
        safe_file_name = ''.join([c for c in nombre_video if c.isalpha() or c.isdigit() or c in [' ', '-', '_']]).rstrip()
        path_final = stream.download(output_path='audio_salida', filename=f'{safe_file_name}.mp3')
        print(f'Audio descargado y guardado en {path_final}')
    except Exception as e:
        print(f'Error descargando de {url}: {str(e)}')

def nombre_existe(nombre_archivo, nombre_video):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if nombre_video in linea:
                    return True
    except FileNotFoundError:
        return False
    return False


