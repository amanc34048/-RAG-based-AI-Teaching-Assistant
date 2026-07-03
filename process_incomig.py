import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import requests

def create_embedding(text):
    data=requests.post("http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input":text
    })
    emd_data= data.json()['embeddings']
    return emd_data

def inference(prompt):
     r=requests.post("http://localhost:11434/api/generate",json={
        # "model":"deepseek-r1:1.5b",
        "model":"llama3.2",
        "prompt":prompt,
        "stream":False
    })
     
     response=r.json()
     print(response)
     return response


df=joblib.load("embadding.joblib")

incomging=input("write quations: ")
q_embed=create_embedding([incomging])[0]
# print(embed)
similarity=cosine_similarity(np.vstack(df["embedding"]),[q_embed]).flatten()
max_index=similarity.argsort()[::-1][0:3]
# print(max_index)

n_df=df.loc[max_index]
# print(n_df[["no","audio_name","text"]])

prompt = f"""
You are an AI Video Search Assistant.

Your only knowledge source is the provided video subtitle chunks.
Never use your own knowledge or make assumptions.
Answer ONLY from the provided subtitle chunks.

Each subtitle chunk contains:
- Video Number (no)
- Video Title (audio_name)
- Subtitle Text (text)
- Start Time in seconds (start)
- End Time in seconds (end)

Instructions:

1. Read all subtitle chunks carefully.
2. Answer ONLY using the provided subtitle chunks.
3. Do NOT guess, infer, or use outside knowledge.
4. If the retrieved subtitle chunks do not contain enough information to answer the user's question, reply:
   "I couldn't find enough information about this in the uploaded videos."
5. If the user's question is unrelated to the uploaded videos, reply:
   "I can only answer questions related to the uploaded videos."
6. Ignore subtitle chunks that are not relevant to the user's question.
7. If multiple subtitle chunks answer the question, include all relevant videos and timestamps.
8. Preserve the exact Video Number, Video Title, Start Time, and End Time from the provided data.
9. Never invent video numbers, titles, timestamps, or facts.
10. Keep the answer concise, accurate, and easy to understand.
11. Always guide the user to watch the relevant video and timestamp.

Video Subtitle Chunks:
{n_df[["no", "audio_name", "text", "start", "end"]].to_json(orient="records")}

--------------------------------------------------

User Question:
"{incomging}"

Return your response in the following format:

Answer:
<Answer based only on the subtitle chunks>

Relevant Video(s):

1.
Video Number:
Video Title:
Timestamp:
Reason:

2.
Video Number:
Video Title:
Timestamp:
Reason:

Recommendation:
Watch the above timestamp(s) for the relevant information.
"""

with open("prompt.txt","w") as f:
    f.write(prompt)

response=inference(prompt)["response"]

print(response)

with open("response.txt","w") as f:
    f.write(response)

# for index,i in n_df.iterrows():
#     print(index,i["no"],i["audio_name"],i["text"],i["start"],i["end"])
