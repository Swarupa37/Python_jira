from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json
# creating flast  instance
app = Flask(__name__)
@app.route("/createJIRA", methods=["POST"])
def create_JIRA():

    url = "https://swarupashejal37.atlassian.net/rest/api/2/issue"
    API_TOKEN="ATATT3xFfGF0n14EEHbwTwMPw-UR1hxdUi5DAEAzX7Htn849RRsyKdwxdPVBtcrfdzhIYs3LONdP1vFdiHo4F5CU2Gc0ZwduMuvIw8Tz___eCeUtRBJMwwbLVOGxAETCxpxJVHpo0UG7YyMWdyxws8Vy9639cOkltyCyJ-Hl22fdzy-R6whQJAc=BB855860"
    auth = HTTPBasicAuth("swarupa.shejal37@gmail.com", API_TOKEN)

    headers = {
       "Accept": "application/json",
       "Content-Type": "application/json"
    }
    payload = json.dumps( {
       "fields": {
       "description": "Creating jira ticket",
       "issuetype": {
           "id": "10003"
       },
       "project": {
           "key": "SCRUM"
       },
       "summary": "First Jira Ticket",

       },
    "update": {}
       } )
  webhook = request.json
    response = None
    if webhook['comment'].get('body') == "/jira":
#response = requests.request("POST",url,data=payloads,headers=headers, auth=auth)
#return json.dumps(json.loads(response.text), sort_keys=True, indent=4, seperators=(",", ":"))

        response = requests.request(

        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

    else:
        print('Jirs issue will be created if comment include /jira')
#return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
