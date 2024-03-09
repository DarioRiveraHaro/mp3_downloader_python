from pytube import Playlist

def obtener_info_videos_lista_reproduccion(url_lista_reproduccion):
    playlist = Playlist(url_lista_reproduccion)
    # Listas que guardan las URLs y nombres de los videos
    urls = []
    titulos = []
    
    for video in playlist.videos:
        urls.append(video.watch_url)
        titulos.append(video.title)
    
    return urls, titulos

if __name__ == '__main__':
    url_lista_reproduccion = input('Ingrese la URL de la playlist: ')
    urls, titulos = obtener_info_videos_lista_reproduccion(url_lista_reproduccion)
    
    print('Informacion de la lista de reproduccion: ')
    for url, titulo in zip(urls, titulos):
        print(f'Titulo: {titulo}, URL: {url}')