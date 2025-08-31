'''Requests Module in Python'''

import requests
from bs4 import BeautifulSoup

# url="https://www.youtube.com/"
# # response = requests.get("https://www.youtube.com/")

# data={
#     "Name":"Jal",
#     "Branch":"CSD",
#     "Age":18
# }

# response = requests.post("https://jsonplaceholder.typicode.com/posts",json=data)

# print(response.text)
# print(response.status_code)
# print(response.json())

url="https://seosherpa.com/header-tags/"

r=requests.get(url)
# print(r.text)

#bs4 module
soup=BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)