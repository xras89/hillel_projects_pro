import random
import string
from time import perf_counter
from typing import Callable

import httpx
from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

result = None
last_button_push = 0
last_post_call = 0


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

create_random_string: Callable[[int], str] = lambda size: "".join(  # noqa
    [random.choice(string.ascii_letters) for i in range(size)]  # noqa
)  # noqa


@app.post("/exchange-rates")
async def get_information(data=Body()):
    global result
    current_time = perf_counter()
    if current_time - perf_counter() <= 10 and result is not None:  # noqa
        return result
    source = data["source"]
    destination = data["destination"]
    """This endpoint returns the random information"""

    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={source}&to_currency={destination}&apikey=XSN17SDSA5RAM5W2"

    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)
    rate: str = response.json()["Realtime Currency Exchange Rate"][
        "5. Exchange Rate"
    ]

    result = f"Exchange rate for {source} to {destination} is {rate}"
    return result


@app.get("/fetch-market")
async def get_current_market_state():
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=XSN17SDSA5RAM5W2"
    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)
    rate: str = response.json()["Realtime Currency Exchange Rate"][
        "5. Exchange Rate"
    ]
    return {
        "rate": rate,
    }
