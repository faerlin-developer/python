def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("divide by zero")

    return a / b


class Calculator:

    def setup(self):
        pass

    def teardown(self):
        pass

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("divide by zero")

        return a / b


def fetch_weather_data(api_client):
    response = api_client.get("https://api.weather.com/data")
    if response.status_code == 200:
        return response.json()
    else:
        return None
