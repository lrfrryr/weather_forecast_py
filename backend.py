import requests

API_KEY = "aa74fcc9c493a4284f1775f2aa3e1302"


def get_data(place, forecast_days=None, kind=None):
    # call to the api
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:8*forecast_days]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))



