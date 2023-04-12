def convert(amount, from_currency, to_currency, exchange_rates):
    rate_from = exchange_rates[from_currency]
    rate_to = exchange_rates[to_currency]
    return amount * (rate_to / rate_from)
