import requests
import json
URL = "https://gist.githubusercontent.com/tony1223/098e45623c73274f7ae3/raw"

def get(query=""):
    d = {}
    r = requests.get(URL)
    r.encoding = 'utf-8'
    j = json.loads(r.text)
    d['modify'] = j['lastmodify']
    data = j['data']
    new_data = []
    if query == "":
        d['data'] = data
        return d
    else:
        for i in data:
            name_split = list(i['姓名'].replace("○", ""))
            flag = True
            for n in name_split:
                if not (n in query):
                    flag = False
                    break
            if flag:
                new_data.append(i)
        d['data'] = new_data
        return d
