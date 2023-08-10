import json
import requests
payload = {
    "name": "Antonio",
    "last_name": "Ruvalcaba",
    "age": 34
}
with open("my_file.png", "rb") as file:
    content = file.read()

payload["profile_picture"] = content
res = requests.request("POST", "localhost:4000/user", data=json.dumps(payload))

print(res.json())