from fetch_rates import get_exchange_rates
from convert_currency import convert
from format_output import format_result
from config import API_KEY, SUPPORTED_CURRENCIES
from gui import run_gui

def main():
    choice = input("Do you want to use the GUI version? (y/n): ").lower()

    if choice == 'y':
        run_gui()
    else:
        exchange_rates = get_exchange_rates(API_KEY)

        if exchange_rates:
            amount = float(input("Enter the amount: "))
            print(f"Supported currencies: {', '.join(SUPPORTED_CURRENCIES)}")
            from_currency = input("Enter the currency to convert from: ").upper()
            to_currency = input("Enter the currency to convert to: ").upper()

            if from_currency in SUPPORTED_CURRENCIES and to_currency in SUPPORTED_CURRENCIES:
                result = convert(amount, from_currency, to_currency, exchange_rates)
                output = format_result(amount, from_currency, to_currency, result)
                print(output)
            else:
                print("Error: Unsupported currency")
        else:
            print("Error: Unable to fetch exchange rates")

if __name__ == "__main__":
    main()
