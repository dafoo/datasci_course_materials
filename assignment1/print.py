import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
pyresponse = json.load(response)

print type(pyresponse)

print pyresponse.keys()
# print pyresponse['results']
print type(pyresponse['results'])
results = pyresponse['results']

for i in range(10):
  print results[i]["text"]
