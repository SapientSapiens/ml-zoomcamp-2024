import requests

url = 'https://kcs14v14u6.execute-api.eu-north-1.amazonaws.com/test/predict'

data = {'url': 'https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg'}

result = requests.post(url, json=data).json()
print(result)