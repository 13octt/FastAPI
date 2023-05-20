import requests

data = {"temperature": 25.0, "light": 500}
response = requests.post("http://localhost:8000/data/", json=data)
print(response.json())
