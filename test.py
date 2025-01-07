import requests

url = "https://api.naanmudhalvan.tn.gov.in/api/v1/lms/client/token/"

key = "a4dc914faccc4ccb59740570b87370e2"
secret = "36fd2f9dbbea9f28b6743a37486f0ab"

payload = {"client_key" : key,
            "client_secret": secret}

response = requests.request("POST", url, data=payload)

print(response.text)
