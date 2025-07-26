import time

import requests


def fetch_page(api_client):
    return api_client.get("https://google.com")


def long_running_task():
    time.sleep(5)
    return "Task Complete"


def process_payment(payment_gateway, amount):
    response = payment_gateway.charge(amount)
    if response == "Success":
        return "Payment processed successfully"
    else:
        raise ValueError("Payment failed")


def main():
    response = fetch_page(requests)
    print(response.content)


if __name__ == "__main__":
    main()
