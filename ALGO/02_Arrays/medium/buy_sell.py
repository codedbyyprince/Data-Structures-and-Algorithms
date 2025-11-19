def buy_sell_stock(arr):
    n = len(arr)
    min_price = arr[0]
    max_profit = 0
    for i in arr:
        profit = i - min_price
        min_price = min(min_price, i)
    return max_profit