import sys
import requests
import json
import pprint

fin = open('fake_email.txt')
text = "".join(fin.readlines()).replace('\n', ' ')
apiKey = 'r5blryDi26DwJSPkbo10WSuwfn_fZga8bt2-Rva1V65p'
endpoint = 'https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/9b221331-af3e-4c86-a0cf-40164afbacae/v3/tone?version=2017-09-21'
payload = json.dumps({'text': text})

auth = {"apikey": apiKey}

r = requests.post(url=endpoint, auth=('apikey', apiKey), json={'text': text})
r = json.loads(r.text)

for sentence in r['sentences_tone']: 
    for tone in sentence['tones']:
        if tone['tone_id'] == 'sadness':
            print(sentence['text'])
            print('tone: {0}\tscore: {1}'.format(tone['tone_id'], tone['score']))
            print()