import os
import subprocess

files=os.listdir("video")
for index,i in enumerate(files):
    file_split=i.split(" ",1)[1].split(".")[0]
    print(file_split)
    file_name=f"{index+1}_{file_split}"
    subprocess.run(["ffmpeg","-i",f"video/{i}",f"audio/{file_name}.mp3"])