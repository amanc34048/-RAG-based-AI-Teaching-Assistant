import requests
import os 
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_embedding(text):
    data=requests.post("http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input":text
    })
    emd_data= data.json()['embeddings']
    return emd_data

json_file=os.listdir("json")

list_dict=[]
chank_id=0

for josns in json_file:
    with open(f"json/{josns}") as f:
        data=json.load(f)
    
    embaddings=create_embedding([c['text'] for c in data['chunks']])
    
    for i,chank in enumerate(data['chunks']):
        chank["chank id"]=chank_id
        chank["embedding"]=embaddings[i]
        chank_id+=1
        list_dict.append(chank)
    

df=pd.DataFrame.from_records(list_dict)  
print(df)
joblib.dump(df,"embadding.joblib")
