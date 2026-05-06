# Currency Converter CLI (Python)

A simple and reliable command‑line currency converter built in Python.  
It uses the Frankfurter API (European Central Bank rates) to convert amounts between supported currencies in real time.  
No API key required.

## 🚀 Features
- Converts any amount between supported currencies
- Uses real exchange rates from the European Central Bank
- Fast and lightweight (only uses `requests`)
- Works on Windows, macOS, and Linux
- Includes a built‑in command to list all supported currencies
- Clear error handling and professional CLI usage instructions

## 📦 Installation
Clone the repository:

```
git clone https://github.com/armandosanchezco-2026/currency-converter.git
cd currency-converter
```

Install the required dependency:

```
pip install requests
```

## 🧭 Usage
Basic conversion:

```
python converter.py <amount> <from_currency> <to_currency>
```

Example:

```
python converter.py 100 EUR USD
```

Output:

```
100 EUR = 108.52 USD
```

If you run the script without arguments, it will display usage instructions and a full list of supported currencies.

## 💱 Supported Currencies
The converter uses the Frankfurter API, which supports all currencies published by the European Central Bank.

To view the full list directly from the API:

```
python converter.py
```

This will print something like:

```
Supported currencies:
  EUR - Euro
  USD - US Dollar
  GBP - British Pound
  JPY - Japanese Yen
  AUD - Australian Dollar
  CAD - Canadian Dollar
  CHF - Swiss Franc
  NZD - New Zealand Dollar
  ZAR - South African Rand
  TRY - Turkish Lira
  SEK - Swedish Krona
  NOK - Norwegian Krone
  DKK - Danish Krone
  PLN - Polish Zloty
  CZK - Czech Koruna
  HUF - Hungarian Forint
  RON - Romanian Leu
  BGN - Bulgarian Lev
  HRK - Croatian Kuna
  ISK - Icelandic Krona
  RUB - Russian Ruble
  INR - Indian Rupee
  BRL - Brazilian Real
  MXN - Mexican Peso
  CNY - Chinese Yuan
  HKD - Hong Kong Dollar
  SGD - Singapore Dollar
  KRW - South Korean Won
  ILS - Israeli Shekel
```

## 🛠 How It Works
1. The script calls the Frankfurter API to fetch the latest exchange rates.
2. It validates the currency codes provided by the user.
3. It calculates the converted amount using the returned rate.
4. It prints the result in a clean, readable format.
5. If no arguments are provided, it fetches and displays the list of supported currencies.

## 📁 Project Structure
```
currency-converter/
├── converter.py
└── README.md
```

## 📄 License
This project is released under the MIT License.  
You are free to use, modify, and distribute it.
