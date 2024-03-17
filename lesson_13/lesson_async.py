import asyncio
from time import perf_counter


async def bar():
    print(f"I am '{bar.__name__}' BEFORE")
    await asyncio.sleep(3)
    print(f"I am '{bar.__name__}' AFTER")

    return 4


async def foo():
    print(f"I am '{foo.__name__}' BEFORE")
    await asyncio.sleep(1)
    print(f"I am '{foo.__name__}' AFTER")

    return 5


async def main():
    start = perf_counter()
    print(f"I am sync '{main.__name__}'")
    # await bar()
    # await foo()
    tasks = [bar(), foo()]
    results = await asyncio.gather(*tasks)
    print(results)
    print(perf_counter() - start)


asyncio.run(main())