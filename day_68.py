'''Clear the clutter'''

import os

class Naming:
    def __init__(self):
        self.x=0

    def converting(self,a):
        self.file=a
        self.x+=1
        os.rename(f"{self.file}.txt",f"{self.x}.txt")

x= Naming()
x.converting('bdgile')
x.converting('uygwefiugwu')
x.converting('kjwerh')