import requests
import json
import time
import vlc
url = "http://covidtracking.com/api/us"
p = vlc.MediaPlayer("infected.mp3")
start = 0
i=0
while(True):
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text)
    positives = int(json_response[0]['positive'])
    if positives > start:
        print("US infected:",(positives+i))
        p.play()
        start=positives
    else:
        print("no change")
        start=0 #just for testing
        i=i+1
    time.sleep(5)
    p.stop()
    
