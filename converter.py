import requests
import sys

API_URL = "https://api.frankfurter.app/latest"
CURRENCIES_URL = "https://api.frankfurter.app/currencies"

def list_currencies():
    """Fetch and return a dictionary of supported currencies."""
    response = requests.get(CURRENCIES_URL)
    if response.status_code != 200:
        return {"ERROR": "Could not fetch currency list"}
    return response.json()

def convert(amount, from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency == to_currency:
        return amount

    params = {
        "from": from_currency,
        "to": to_currency
    }

    response = requests.get(API_URL, params=params)

    if response.status_code != 200:
        raise Exception("Error fetching exchange rates")

    data = response.json()
    rates = data.get("rates", {})

    if to_currency not in rates:
        raise Exception("Invalid currency code")

    rate = rates[to_currency]
    return amount * rate

def main():
    if len(sys.argv) != 4:
        print("Usage: python converter.py <amount> <from_currency> <to_currency>")
        print("Example: python converter.py 100 EUR USD\n")

        print("Supported currencies:")
        currencies = list_currencies()
        for code, name in currencies.items():
            print(f"  {code} - {name}")
        return

    amount = float(sys.argv[1])
    from_currency = sys.argv[2]
    to_currency = sys.argv[3]

    try:
        result = convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
