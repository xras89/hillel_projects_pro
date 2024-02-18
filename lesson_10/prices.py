import datetime
import json
from dataclasses import dataclass

import requests

ALPHAVANTAGE_API_KEY = "0BT5VATLUGIIX0V4"
MIDDLE_CURRENCY = "CHF"

fulldate = datetime.datetime.now()
timestamp = fulldate.strftime("%d.%m.%y - %H:%M:%S")
log_results = {"results": []}


@dataclass
class Price:
    value: float
    currency: str

    def __add__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(
                value=(self.value + other.value), currency=self.currency
            )

        left_in_middle: float = convert(
            value=self.value,
            currency_from=self.currency,
            currency_to=MIDDLE_CURRENCY,
        )
        right_in_middle: float = convert(
            value=other.value,
            currency_from=other.currency,
            currency_to=MIDDLE_CURRENCY,
        )

        total_in_middle: float = left_in_middle + right_in_middle
        total_in_left_currency: float = convert(
            value=total_in_middle,
            currency_from=MIDDLE_CURRENCY,
            currency_to=self.currency,
        )

        return Price(value=total_in_left_currency, currency=self.currency)


def log_format_results(
    currency_from: str, currency_to: str, rate: float, date: str
):
    log_content: dict = {
        "currency_from": currency_from,
        "currency_to": currency_to,
        "rate": rate,
        "timestamp": date,
    }
    log_results["results"].append(log_content)


def convert(value: float, currency_from: str, currency_to: str) -> float:
    URL = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_from}&to_currency={currency_to}&apikey={ALPHAVANTAGE_API_KEY}"  # noqa
    response: requests.Response = requests.get(URL)
    result: dict = response.json()
    # Response example
    # {
    #     "Realtime Currency Exchange Rate": {
    #         "1. From_Currency Code": "UAH",
    #         "2. From_Currency Name": "Ukrainian Hryvnia",
    #         "3. To_Currency Code": "USD",
    #         "4. To_Currency Name": "United States Dollar",
    #         "5. Exchange Rate": "0.02648000",
    #         "6. Last Refreshed": "2024-02-12 19:04:02",
    #         "7. Time Zone": "UTC",
    #         "8. Bid Price": "0.02647900",
    #         "9. Ask Price": "0.02648000"
    #     }
    # }
    # print(result)
    coefficient: float = float(
        result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    )

    log_format_results(
        currency_from=currency_from,
        currency_to=currency_to,
        rate=coefficient,
        date=timestamp,
    )

    return round(value * coefficient, 2)


flight = Price(value=700, currency="USD")
hotel = Price(value=21300, currency="UAH")

total: Price = flight + hotel
print(total)

with open("logs.json", mode="a") as file:
    json.dump(log_results, file, indent=4)
