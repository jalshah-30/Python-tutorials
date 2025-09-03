'''AsyncIO in Python'''
import time
import asyncio
import requests

# URL="https://instagram.com/favicon.ico"
# response=requests.get(URL)
# open("instagram.ico","wb").write(response.content)

async def function1():
    URL="https://wallpapershome.com/images/pages/pic_h/12465.jpg"
    response=requests.get(URL)
    open("Wallpaper1.jpg","wb").write(response.content)
    await asyncio.sleep(1)
    print("Function 1")

async def function2():
    URL="https://static.vecteezy.com/system/resources/previews/033/331/606/non_2x/samurai-fighting-silhouette-wallpaper-4k-desktop-samurai-fighting-background-cool-vibe-and-full-moon-landscape-view-illustration-background-vector.jpg"
    response=requests.get(URL)
    open("wallpaper2.jgp","wb").write(response.content)
    await asyncio.sleep(1)
    print("Function 2")
    return "Jal"

async def function3():
    URL="https://instagram.com/favicon.ico"
    response=requests.get(URL)
    open("instagram3.ico","wb").write(response.content)
    await asyncio.sleep(4)
    print("Function 3")

async def main():

    await function1()
    await function2()
    await function3()

    # L = await asyncio.gather(
    #     function1(),
    #     function2(),
    #     function3(),
    # )
    # print(L)


    # task=asyncio.create_task(function1())
    # # await function1()
    # await function2()
    # await function3()

asyncio.run(main())

