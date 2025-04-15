# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://localhost:8083/rest/api/2/project"

API_TOKEN="MzQ0MDU1NjY0MjQ5OlCB8WYH75MWDUziQG3qTcj8CJNO"

auth = HTTPBasicAuth("swarupa.shejal37@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
