import datetime
import asyncio

async def print_x():
    x = 0
    while True:
        x+=4
        await asyncio.sleep(4)
        print(f"{x} seconds have passed {datetime.datetime.now().strftime('%I:%M %p')}")
        

async def print_y():
    y = 0
    while True:
        y += 6
        await asyncio.sleep(6)
        print(f"{y} seconds have passed")


async def main():
    task_x = asyncio.create_task(print_x())
    task_y = asyncio.create_task(print_y())
    await asyncio.gather(task_x, task_y)
    # await pauses the exection of whatever it is in while it does the specified functions

asyncio.run(main())