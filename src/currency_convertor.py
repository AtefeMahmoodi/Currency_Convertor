import requests
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=3*60*60)

@cached(cache)
def get_exchange_rate(base_currency : str, target_currency : str) -> float:
    """The function to find the exchange rate between two currencies

    :param base_currency: The base currency you want to exchange
    :param target_currency: The target currency you want to exchange to
    :return: The exchange rate
    """
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base_currency}")
    if response.status_code != 200:
        return None
    else:
        return response.json()['rates'][f'{target_currency}']
    

def convert_amount(exchange_rate : float, amount : float) -> float:
    """The method for converting a specific amount of money

    :param exchange_rate: The exchange rate between two currencies you have chsen before
    :param amount: The amount of money you want to convert
    :return: The converted amount
    """
    return exchange_rate * amount
    

if __name__ == '__main__':
    base_currency = input("Enter base currency: ")
    target_currency = input("Enter target currency: ")
    amount = float(input("Enter amount: "))
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = convert_amount(amount, exchange_rate)
    print(f"{amount} {base_currency} is {converted_amount} {target_currency}")