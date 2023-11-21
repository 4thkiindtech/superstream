import os
import subprocess

# Specify source directory and proxy format
source_directory = "/path/to/source/media"
proxy_format = "h264_1080p_proxy.mp4"

# Traverse source directory
for root, dirs, files in os.walk(source_directory):
    for file in files:
        # Check if file is a video
        if file.lower().endswith(('.mov', '.mp4', '.avi', '.mkv', '.flv', '.wmv')):
            # Get source file path
            source_file = os.path.join(root, file)

            # Create destination directory
            dest_directory = root.replace(source_directory, "/path/to/proxy/media")
            if not os.path.exists(dest_directory):
                os.makedirs(dest_directory)

            # Get proxy file path
            proxy_file = os.path.join(dest_directory, file)

            # Create proxy using FFmpeg
            subprocess.call(['ffmpeg', '-i', source_file, '-vf', 'scale=-1:1080', '-c:v', 'libx264', '-preset', 'medium', '-crf', '23', '-c:a', 'copy', proxy_file])

print("Proxy creation complete.")