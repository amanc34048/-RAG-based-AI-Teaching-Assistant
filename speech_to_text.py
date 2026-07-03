import whisper
import json
model=whisper.load_model("large-v2")
result=model.transcribe(audio="audio/1_1 video.mp3",
                        language="hi",
                        task="translate",
                        word_timestamps=False)
# print(result['segments'])

chanks=[]
for i in result['segments']:
    chanks.append({"start":i['start'],"end":i['end'],"text":i['text']})

print(chanks)
with open("output.json","w") as f:
    json.dump(chanks,f)