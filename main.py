import subprocess

input_file = 'input.webm'
output_file = 'output.mov'

# Команда для FFmpeg с использованием кодека H.264 для видео
ffmpeg_command = f'ffmpeg -i {input_file} -c:v libx264 -pix_fmt yuv420p -c:a pcm_s16le -strict experimental -q:a 0 {output_file}'

# Вызов команды через subprocess
subprocess.run(ffmpeg_command, shell = True)
