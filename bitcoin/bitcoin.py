import requests
import sys


def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        price_per_bitcoin = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Request failed")

    total_cost = bitcoins * price_per_bitcoin
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()

