import asyncio
import time

async def test():
    print(time.time())
    await asyncio.sleep(1)
    print(time.time())

# asyncio.run(test())

asyncio.new_event_loop().run_until_complete(test())