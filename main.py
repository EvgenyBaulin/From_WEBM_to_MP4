import subprocess

# input_file = 'input.webm'
# output_file = 'output.mov'

input_file = input('Path to input file: ')
output_file = input('Path to output file: ')

is_hdr = input('Input file in HDR?\nYes/No: ')

if is_hdr == 'Yes':
	ffmpeg_command = f'ffmpeg -i {input_file} -c:v libx264 -pix_fmt yuv420p -c:a pcm_s16le -strict experimental -q:a 0 {output_file}'
else:
	ffmpeg_command = f'ffmpeg -i {input_file} -c:v prores_ks -profile:v 3 -c:a pcm_s16le -q:a 0 {output_file}'

subprocess.run(ffmpeg_command, shell = True)
