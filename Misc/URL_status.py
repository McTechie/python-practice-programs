import requests

url = input("Enter URL : ")

response = requests.get(url)
response.raise_for_status()
