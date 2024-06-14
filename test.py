import requests

# How to consume the API from a python script
response = requests.get('http://localhost:8000/playground/api/posts')
print(response.json())