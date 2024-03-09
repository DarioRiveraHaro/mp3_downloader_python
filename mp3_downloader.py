from pytube import YouTube
import os

def download_youtube_audio(url, output_path, file_name):
    # Download the YouTube video
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    audio_file_path = stream.download(output_path=output_path, filename='temp_audio')

    # Rename the downloaded file to have a .mp3 extension
    os.rename(audio_file_path, os.path.join(output_path, f'{file_name}.mp3'))
    print(f'Audio descargado y guardado como {os.path.join(output_path, "output.mp3")}')

if __name__ == '__main__':
    url = input('Ingrese la URL del video de YouTube: ')
    file_name = input('Ingrese el nombre de la cancion: ')
    output_path = 'audio_salida'
    download_youtube_audio(url, output_path, file_name)
