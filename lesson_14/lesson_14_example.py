import asyncio
import random
import sys  # sys.argv возвращает список,в котором 1й элемент - это абсолютный путь к данному файлу # noqa
from pprint import pprint as print
from threading import Thread
from time import perf_counter
from typing import Coroutine

import httpx
import requests

# from multiprocessing import Queue

POKEAPI_URL_ADDRESS: str = "https://pokeapi.co/api/v2/pokemon"
# POKEMONS = []


def fetch_pokemon(id_: int) -> dict:
    """Fetching the detailed pokemon info from the PokeAPI.co"""
    response: requests.Response = requests.get(
        url=f"{POKEAPI_URL_ADDRESS}/{id_}"
    )
    if response.status_code != 200:
        print(f"Error: {response.status_code} | {response.text}")
        return {}
    else:
        # POKEMONS.append(response.json())
        print(response.status_code)
        return response.json()


def main_sync(pokemons_number: int):
    results: list[dict] = []
    for _ in range(pokemons_number):
        random_id: int = random.randint(1, 50)
        pokemon: dict = fetch_pokemon(id_=random_id)
        results.append(pokemon)
    return results


def main_threads(pokemons_number: int):
    """Fetch pokemons using threads"""
    # results: list[dict] = []
    threads: list[Thread] = []
    for _ in range(pokemons_number):
        random_id = random.randint(1, 50)
        threads.append(Thread(target=fetch_pokemon, args=(random_id,)))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


async def main_async(pokemons_number: int):
    # tasks = [asyncio.to_thread(fetch_pokemon, id_=random.randint(1, 50))
    #         for i in range(pokemons_number)
    #     ]
    # response = await asyncio.gather(*tasks)
    # print(response.status_code)
    async def get_with_httpx(url: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            print(response.status_code)
            return response.status_code

    tasks: list[Coroutine] = [
        get_with_httpx(url=f"{POKEAPI_URL_ADDRESS}/{random.randint(1, 50)}")
        for i in range(pokemons_number)
    ]
    results = await asyncio.gather(*tasks)
    return results


def main():
    try:
        runtype: str = sys.argv[1]
        pokemons_number: int = int(sys.argv[2])
    except IndexError:
        print("No such pokemon")
    except ValueError:
        print("You should use integers")

    if runtype == "sync":
        main_sync(pokemons_number)
    elif runtype == "threads":
        main_threads(pokemons_number)
    elif runtype == "async":
        asyncio.run(main_async(pokemons_number))

    else:
        raise SystemExit("Unrecognized command")


if __name__ == "__main__":
    start = perf_counter()
    main()
    finish = perf_counter() - start
    print(f"{finish=}")


# time python -m lesson sync 15 запуск в терминале. тайм прописан в алиасе