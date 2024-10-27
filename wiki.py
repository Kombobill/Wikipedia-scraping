import requests

# Making a GET request
r = requests.get('https://en.wikipedia.org/wiki/Kenya')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)