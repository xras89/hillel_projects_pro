input_data = "100 UAH"


# Stripe
# 100 UAH -> CHF

currency_exchange = {
    "CHF": 1,
    "USD": 0.87,
    "EUR": 0.94,
    "UAH": 0.023,
    "GBP": 1.10,
    "PLN": 0.22,
}


class Price:
    def __init__(self, value: int, currency: str):
        self.value = value
        self.currency = currency

    def __str__(self):
        return f"{self.value} {self.currency}"

    def __add__(self, other) -> "Price":
        if self.currency == other.currency:
            return Price(self.value + other.value, self.currency)
        else:
            self.value = self.value * currency_exchange[self.currency]
            other.value = other.value * currency_exchange[other.currency]
            return Price(
                round(
                    (self.value + other.value)
                    / currency_exchange[self.currency],
                    2,
                ),
                self.currency,
            )

    def __sub__(self, other) -> "Price":
        if self.currency == other.currency:
            return Price(self.value - other.value, self.currency)
        else:
            self.value = self.value * currency_exchange[self.currency]
            other.value = other.value * currency_exchange[other.currency]
            return Price(
                round(
                    (self.value - other.value)
                    / currency_exchange[self.currency],
                    2,
                ),
                self.currency,
            )


class Product:
    def __init__(self, name: str, price: Price):
        self.name = name
        self.price = price


class PaymentProcessor:
    def checkout(self, product: Product, price: Price):
        pass


# Tests #1
flight = Price(value=200, currency="USD")
hotel = Price(value=1000, currency="EUR")
total: Price = flight + hotel
# total.currency == USD
print(total)

# Tests #2
book = Price(value=1000, currency="UAH")
food = Price(value=100, currency="USD")
total: Price = book + food
# total.currency == UAH
print(total)

# Tests #3
apple = Price(value=150, currency="EUR")
banana = Price(value=100, currency="EUR")
total: Price = apple - banana
# total.currency == EUR
print(total)

# Tests #4
phone = Price(value=3500, currency="PLN")
charger = Price(value=10, currency="USD")
total: Price = phone - charger
# total.currency == PLN
print(total)
