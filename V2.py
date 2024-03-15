from pytube import YouTube, Playlist

# Función para verificar si un archivo ya existe en un archivo de texto
def nombre_existe(nombre_archivo, nombre_video):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if nombre_video in linea:
                    return True
    except FileNotFoundError:
        # Si el archivo no existe, retorna False
        return False
    return False

# Descargar el audio de un video de youtube
def decargar_audio(url, nombre_archivo):
    if nombre_existe('nombre_videos.txt', nombre_archivo):
        print(f"La cancion {nombre_archivo} ya fue descargada. Saltando descarga...")
        return

    # Escribir el nombre del video en un archivo de texto
    with open('nombre_videos.txt', 'a') as archivo:
        archivo.write(f"{nombre_archivo}\n")
        
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        safe_file_name = ''.join([c for c in nombre_archivo if c.isalpha() or c.isdigit() or c in [' ', '-', '_']]).rstrip()
        path_final = stream.download(output_path='audio_salida', filename=f"{safe_file_name}.mp3")
        print(f"Audio descargado y guardado en {path_final}")

    except Exception as e:
        print(f"Error descargando de {url}: {str(e)}")
        
# Funcion para obtener la playlist de youtube
def obtener_info_videos_lista_reproduccion(url_lista_reproduccion):
    playlist = Playlist(url_lista_reproduccion)
    print(f'Descargando {len(playlist.video_urls)} videos de la playlist.')
    
    # Recorre toda la playlist cancion por cancion y manda a llamar a la funcion que descarga la cancion.
    for video in playlist.videos:
        url = video.watch_url
        titulo = video.title
        print(f"Descargando el audio de: {titulo} - {url}")
        decargar_audio(url, titulo)

# Inicia el scrip preguntando por una url de una playlist.
if __name__ == '__main__':
    playlist_url = input('Ingrese la URL de la playlist: ')
    obtener_info_videos_lista_reproduccion(playlist_url)
