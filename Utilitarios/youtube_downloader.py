import yt_dlp

def yt_to_mp4(video_link):
    url = video_link
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo = título do vídeo
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        video_title = info.get('title', 'audio_sem_nome')
        ydl.download([url])  # Baixa e converte para MP3

    print(f"Áudio baixado: {video_title}.mp4")



def yt_to_mp3(video_link):
    url = video_link
    
    # Configurações para extrair o áudio e nomear o arquivo com o título
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo = título do vídeo
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        video_title = info.get('title', 'audio_sem_nome')
        ydl.download([url])  # Baixa e converte para MP3

    print(f"Áudio baixado: {video_title}.mp3")