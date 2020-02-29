import requests

url="https://jsonplaceholder.typicode.com/posts/1"

response=requests.delete(url)
print(response.text,response.status_code)
assert response.status_code==200