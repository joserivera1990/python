import requests
import json

resp = requests.get('http://httpbin.org/get')

print(resp.json())

respJson = resp.json()

respHeaders = respJson.get("headers")

respHeadersPostmanToken = respHeaders.get("Accept-Encoding")

print(respHeadersPostmanToken)

respHeadersPostmanTokenSplit = respHeadersPostmanToken.split(",")
print(len(respHeadersPostmanTokenSplit))
print(respHeadersPostmanTokenSplit)

if len(respHeadersPostmanTokenSplit) > 1:
  print(respHeadersPostmanTokenSplit[0])
  print(respHeadersPostmanTokenSplit[1])
else:
  raise Exception("No exist data")

respPost = requests.post('https://httpbin.org/post', data = json.dumps(respHeadersPostmanToken.upper()))

print(respPost.json())
