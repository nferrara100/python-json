import math

import requests


def get_places(lat, long):
    url = "https://api.foursquare.com/v3/places/search"
    params = {
        "query": "lunch",
        "ll": f"{lat},{long}",
    }
    headers = {
        "Accept": "application/json",
        "Authorization": "fsq38jf5s6BtxsM5GasJ/3pdhr7HlOSL2O6cjpiwegCvd90=",
    }
    response = requests.request("GET", url, params=params, headers=headers)

    json = response.json()
    results = json["results"]
    normalised = [
        {
            "name": x["name"],
            "distance": x["distance"],
            "lat": x["geocodes"]["main"]["latitude"],
            "long": x["geocodes"]["main"]["longitude"],
        }
        for x in results
    ]

    ordered = dict(
        sorted(
            normalised.items(),
            lambda x: math.sqrt((long - x["long"]) ** 2 + (lat - x["lat"]) ** 2),
        )
    )
    # sqrt(
    #     (origin[0] - destination[0])**2
    #     + (origin[1] - destination[1])**2
    # )

    return ordered
