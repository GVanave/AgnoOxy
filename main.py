

import json
import requests
import os

from dotenv import load_dotenv
load_dotenv()

def search(query, n_results=5):
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json().get('organic', [])

    string = []
    for result in results[:n_results]:
        try:
            string.append('\n'.join([
                f"Title: {result['title']}", f"Link: {result['link']}",
                f"Snippet: {result['snippet']}", "\n-----------------"
            ]))
        except KeyError:
            continue  # Skip missing data

    return string
ouptut = search("Which teams are playing today the first IPL match?")

print(ouptut)



# import http.client
# import json

# conn = http.client.HTTPSConnection("google.serper.dev")
# payload = json.dumps({
#   "q": "linkedin"
# })
# headers = {
#   'X-API-KEY': 'a1fb2e2c17afe29ab53304180fd743c259ade54a',
#   'Content-Type': 'application/json'
# }
# conn.request("POST", "/search", payload, headers)
# res = conn.getresponse()
# data = res.read()
# data = data.decode("utf-8")

# print(data)


#### next goal is to access specific job wbsite using the agent and try to u