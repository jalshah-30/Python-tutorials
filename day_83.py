import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

x=int(input("Enter to how many you want to wish:"))

name_list=[]
for i in range(x):
    name=input("Enter name:")
    name_list.append(name)

for n in name_list:
    speaker.Speak(f"Good Morning {n}")