from youtube_downloader import yt_to_mp3, yt_to_mp4
import os

while True:
    os.system('cls')
    escolha = input("Escolha o que deseja fazer:\n"
                        "1. Baixar vídeo do youtube\n"
                        "2. Baixar áudio do youtube\n"
                        "C. Fechar o programa\n"
                        "Escolha: ")
    
    if escolha == "1":
        url = input("Digite o link do vídeo que quer baixar: ")
        yt_to_mp4(url)
    elif escolha == "2":
        url = input("Digite o link do audio que quer baixar: ")
        yt_to_mp3(url)
    elif escolha == "c":
        break