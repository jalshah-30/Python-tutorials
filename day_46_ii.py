import os
if(not os.path.exists("Data")):
    os.mkdir("Data")

for i in range(1,101):
    os.rename(f"Data/Day{i}",f"Data/Tutorial{i}")