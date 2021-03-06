#!/bin/python3
# https://www.hackerrank.com/challenges/stockmax/problem
import os


# Complete the stockmax function below.
def stockmax(prices):
    profit = 0
    sorted_prices = prices[:]
    sorted_prices.sort(reverse=True)

    for price in prices:
        max_price = sorted_prices[0]
        if price == max_price:
            del sorted_prices[0]
            continue
        elif price < max_price:
            profit += (max_price - price)

        sorted_prices.remove(price)
    return profit


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
