import os
import sys
import moviepy.editor as mp

# directorio principal
main_directory = os.getcwd()

# directorio de video
video_path = os.path.join(main_directory, 'video/')

# directorio de audio
audio_path = os.path.join(main_directory, "audio")

# verificar si existen los directorios, si no, crearlos

# obtiene los argumentos desde terminal
video_input = sys.argv[1]
name_input = sys.argv[2]
path_video_file = os.path.join(video_path, video_input)

if len(sys.argv) == 3:
    # Procesa el video
    video = mp.VideoFileClip(f"{path_video_file}").subclip(0)

if len(sys.argv) == 5:
    # Toma los argumentos del tiempo
    t_start = int(sys.argv[3])
    t_end = int(sys.argv[4])
    # Procesa el video
    video = mp.VideoFileClip(f"{path_video_file}").subclip(t_start, t_end)

# audio path
path_audio_file = os.path.join(audio_path, name_input)
# convert to audio
video.audio.write_audiofile(path_audio_file+".mp3")
print('Conversion terminada!')

video.close()
