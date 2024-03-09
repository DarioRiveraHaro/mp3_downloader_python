from pytube import YouTube
from pytube import Playlist

# Descargar el audio de un video de youtube
def download_youtube_audio(url, file_name):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        safe_file_name = ''.join([c for c in file_name if c.isalpha() or c.isdigit() or c in [' ', '-', '_']]).rstrip()
        final_path = stream.download(output_path='audio_salida', filename=f"{safe_file_name}.mp3")
        print(f"Audio downloaded and saved as {final_path}")
    except Exception as e:
        print(f"Error downloading audio from {url}: {str(e)}")

def obtener_info_videos_lista_reproduccion(url_lista_reproduccion):
    playlist = Playlist(url_lista_reproduccion)
    print(f'Downloading {len(playlist.video_urls)} videos from the playlist.')
    
    for video in playlist.videos:
        url = video.watch_url
        titulo = video.title
        print(f"Downloading audio from: {titulo} - {url}")
        download_youtube_audio(url, titulo)

if __name__ == '__main__':
    playlist_url = input('Ingrese la URL de la playlist: ')
    obtener_info_videos_lista_reproduccion(playlist_url)
