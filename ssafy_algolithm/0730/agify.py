import requests
name = input()
url = f"https://api.agify.io/?name={name}"
response = requests.get(url).json()
print(response)

