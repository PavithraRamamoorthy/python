import requests
response=requests.get("http://dummy.restapiexample.com/api/v1/employees")
print(response.text)



