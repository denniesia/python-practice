def exchange_money(budget:float, exchange_rate:float):
    return budget / exchange_rate

def get_change(budget:float, exchanging_value:float):
    return budget - exchanging_value

def get_value_of_bills(denomination:float, number_of_bills:int):
    total = denomination * number_of_bills
    return int(total // denomination * denomination)

def get_number_of_bills(amount: float, denomination:int):
    return int(amount // denomination)

def get_leftover_of_bills(amount:float, denomination:int):
    return amount % denomination

def exchangeable_value(budget:float, exchange_rate:float, spread: int, denomination:int):
    exchange_rate *=  1 + (spread / 100)
    new_currency = exchange_money(budget, exchange_rate)
    number_of_bills = get_number_of_bills(new_currency, denomination)
    return get_value_of_bills(denomination, number_of_bills)




