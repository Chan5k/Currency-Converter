import requests

def get_exchange_rates(api_key):
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["rates"]
    else:
        return None
