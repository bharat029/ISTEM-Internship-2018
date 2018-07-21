# modules to be imported 
import json
import string
import requests

# getting the input from the relevant file
fp = open("finalDataSet_2.txt", "r")
line = fp.readline()
out = []
count = 1
while (line) :
	line = line.rstrip("\n")
	out.append({'id' : str(count), 'language' : 'en', 'text' : str(line)})
	count = count + 1
	line = fp.readline()
fp.close()

# string which will be passed to the functions for key-features extraction 
documents = {'documents' : out}

# subscription key and base url
subscription_key = "a1cd3c4c72724acfb1906f6462367099"
assert subscription_key
text_analytics_base_url =  "https://australiaeast.api.cognitive.microsoft.com/text/analytics/v2.0/" 
key_phrase_api_url = text_analytics_base_url + "keyPhrases"
headers   = {'Ocp-Apim-Subscription-Key': subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()
print(key_phrases)
# end of file 