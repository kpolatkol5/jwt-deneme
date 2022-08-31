from email import header
from wsgiref import headers
import requests
from pprint import pprint

def client():
    Authorization= "Authorization eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNzIwNDE1LCJpYXQiOjE2NjE3MjAxMTUsImp0aSI6IjY1YTJiYTdiNmI3ODQ3N2FhYTlmNzQ1ZTY4MmY1MmVkIiwidXNlcl9pZCI6MX0.jWuYLnRnkr4XVKLkTU54K8I5K4bpHpD8D_qyIXtKHVA"

    headers = {
            "Authorization": Authorization,
        }

    response = requests.get(
        url = "http://127.0.0.1:8000/api/rest-auth/login/",
        headers = headers,
    )

    print(f"Status Code: {response.status_code}")
    response_data = response.json()
    pprint(response_data)

if __name__ == "__main__":
    client()