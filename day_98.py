#MultiProcessing in Python

import multiprocessing
import requests

def DownloadFile(url,name):
    response=requests.get(url)
    open(f"files/file{name}.jpg","wb").write(response.content)

url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1AKF7LelsXtbK8YAYYdiPrDMZdFd74ZTgkQ&s"

for i in range(5):
    DownloadFile(url,i)
    p= multiprocessing.Process(target=DownloadFile,args=[url,i])
    p.start()