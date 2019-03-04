
def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    for current_price in stock_prices[1:]:
        potential_profit = current_price - min_price
        if potential_profit > max_profit:
            max_profit = potential_profit
        if current_price < min_price:
            min_price = current_price

    return max_profit
