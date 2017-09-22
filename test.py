import asyncio
import random

async def lazy_func(msg, delay=1):
    print(msg, "will be displayed in", delay, "seconds")
    await asyncio.sleep(delay)
    return msg.upper()

async def time_log():
    i = 0
    print("time log started")
    while True:
        await asyncio.sleep(1)
        i += 1
        print("...%02d sec" % (i, ))

async def main():
    t = asyncio.ensure_future(time_log())
    messages = ['hello', 'world', 'apple', 'banana', 'cherry']
    fts = [asyncio.ensure_future(lazy_func(msg, random.randrange(1, 5))) for msg in messages]
    # result = await asyncio.gather(*fts)
    # t.cancel()
    # print(result)

    for f in asyncio.as_completed(fts):
        result = await f
        print(result)
    t.cancel()

    # (done, pending) = await asyncio.wait(fts, timeout=2)
    # if pending:
    #     print(type(pending))
    #     print("there are {} tasks not completed yet".format(len(pending)))
    #     for f in pending:
    #         f.cancel()
    # for f in done:
    #     x = await f
    # print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()