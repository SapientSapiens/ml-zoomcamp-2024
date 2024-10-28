import requests

url = 'http://localhost:9696/subs_predict'

# Given client data
client = {"job": "student", "duration": 280, "poutcome": "failure"}

response = requests.post(url, json=client).json()
#print('Inside subs-prob-test.py', response)

if response['subscription'] == True:
    print('The client may subscribe to a term deposit. High probability value of %s' % response['subscription_probability'])
else:
    print('The client may not subscribe to a term deposit. Low probability value of %s' % response['subscription_probability'])