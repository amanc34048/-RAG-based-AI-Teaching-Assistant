import whisper
import json
import os

model=whisper.load_model("large-v2")
audio=os.listdir("audio")

for aud in audio:
        if("_" in aud):
                aud_no=aud.split("_")[0]
                aud_name=aud.split("_",1)[1].split(".")[0]
                print(aud_no,aud_name)
                result=model.transcribe(audio=f"audio/{aud}",
                        language="hi",
                        task="translate",
                        word_timestamps=False)
                print(result['segments'])

                chanks=[]
                for i in result['segments']:
                        chanks.append({"no":aud_no,"audio_name":aud_name,"start":i['start'],"end":i['end'],"text":i['text']})
                        chunk_all_data={"chunks":chanks,"result":result["text"]}

                        with open(f"json/{aud}.json","w") as f:
                                json.dump(chunk_all_data,f)