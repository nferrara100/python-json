import json

results = [
    {
        "destination": "LGW",
        "origin": "JFK",
        "arrival_time": "17:50",
        "departure_time": "18:00",
        "price": "432GBP",
        "source": "duffel_air",
    },
    {
        "flights": "JFK/LGW",
        "arrival_time": "17:50",
        "departure_time": "18:00",
        "price_fractional": "12300",
        "currency_code": "GBP",
        "source": "virgin",
    },
    {
        "flights": "JFK/LGW",
        "arrival_time": "19:30",
        "departure_time": "15:00",
        "price_fractional": "10900",
        "currency_code": "GBP",
        "source": "virgin",
    },
    {
        "destination_code": "lgw",
        "origin_code": "jfk",
        "arrival_datetime": "2020-07-23 12:07:53 +0000",
        "departure_time": "2020-07-23 09:01:20 +0000",
        "price": {"code": "USD", "value": "325.50"},
        "source": "aa",
    },
    {
        "destination_code": "lgw",
        "origin_code": "jfk",
        "duration": "542",
        "take_off_at": "2020-07-23 09:01:20 +0000",
        "price": {"code": "GBP", "value": "425.50"},
        "source": "ba",
    },
]

for result in results:
    if result["source"] == "virgin":
        result["price_norm"] = int(result["price_fractional"][:-3])
        # result["currency"]  result[""]
    if result["source"] == "duffel_air":
        result["price_norm"] = int(result["price"][:-3])
    if result["source"] == "aa":
        result["price_norm"] = int(result["price"]["value"][:-3])
    if result["source"] == "ba":
        result["price_norm"] = int(result["price"]["value"][:-3])

final = sorted(results, key=lambda result: result["price_norm"])

print(json.dumps(final, indent=2, sort_keys=True))
