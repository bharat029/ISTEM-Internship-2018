import json
 
fhand = open('finalDataSet_2.txt')
 
data = fhand.readlines()
json_data = {"documents" : []}
id = 1
 
for line in data:
    temp = {"language" : "en", "id" : str(id), "text" : line}
    json_data["documents"].append(temp)
    id += 1
     
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{a1cd3c4c72724acfb1906f6462367099}',
}

params = urllib.parse.urlencode(json_data)

try:
    conn = http.client.HTTPSConnection('australiaeast.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases')
    conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
