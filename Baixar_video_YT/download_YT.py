#opção01: !pip install pytube
#opção02: pip install --upgrade youtube-dl
#pip install ffmpeg-python

from pytube import YouTube
import easygui
import ffmpeg
import os

# url_video = "https://www.youtube.com/watch?v=UddrdePhbfM"
url_video = input("Informe a url do video: ")

try:
    yt = YouTube(url_video)
    diretorio = easygui.diropenbox().replace("'\'", "'/'")

    # coletando as informações do video para saber as TAGS que serão utilizadas
    dict_video_info = yt.vid_info
    lst_straemingData = dict_video_info['streamingData']
    lst_adaptiveFormats = lst_straemingData['adaptiveFormats']

    # Pegando o título do video
    titulo_video = dict_video_info['videoDetails']['title']

    # Pega o tipo de resolução disponível no vídeo
    lst_qualidade = []
    for indice in range(len(lst_adaptiveFormats)):
        dict_adaptiveFormats_indice = lst_adaptiveFormats[indice]
        for chave in dict_adaptiveFormats_indice:
            qualidade = dict_adaptiveFormats_indice[chave]
            if chave == 'height':
                if qualidade not in lst_qualidade:
                    lst_qualidade.append(qualidade)

    print("Informe a qualidade do video que deseja baixar:")
    for indice in range(len(lst_qualidade)):
        print(f"{' ' * 10}Digite {indice + 1} para {lst_qualidade[indice]}p")

    qualidade_selecionada = (int(input("Opção escolhida: ")) - 1)
    print("Fazendo download do video...")
    yt.streams.filter(resolution=str(lst_qualidade[qualidade_selecionada]) + "p",
                      file_extension="mp4").first().download(diretorio,
                                                             filename=f"{titulo_video}_video.mp4")

    print("Fazendo download do audio...")
    indice_audio = yt.streams.filter(only_audio=True).get_audio_only().itag
    yt.streams.get_by_itag(indice_audio).download(diretorio,
                                                  filename=f"{titulo_video}_audio.mp4")

    print("Fazendo a junção do video e do audio...")
    video_YT = ffmpeg.input(f"{diretorio}/{titulo_video}_video.mp4")
    audio_YT = ffmpeg.input(f"{diretorio}/{titulo_video}_audio.mp4")
    ffmpeg.output(video_YT,
                  audio_YT,
                  f'{diretorio}/{titulo_video}.mp4').run()
    remover_video = f"{diretorio}/{titulo_video}_video.mp4"
    remover_audio = f"{diretorio}/{titulo_video}_audio.mp4"
    os.remove(remover_video)
    os.remove(remover_audio)
    print("Concluído!")
except:
    print("Connection Error")