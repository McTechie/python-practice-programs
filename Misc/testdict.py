import os
import requests

dirs = os.listdir()
dict1 = {}
c=0

for file in dirs:
    if file == "sample.txt":
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                s = line.strip()
                c=c+1
                if c==1 : dict1["title"] = s
                elif c==2 : dict1["name"] = s
                elif c==3 : dict1["date"] = s
                else: dict1["feedback"] = s
print (dict1)
