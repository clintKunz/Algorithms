#!/usr/bin/python

import sys

def making_change(amount, denominations=[1, 5, 10, 25, 50], cache=None):
  # 1-4 is 1
  # 1a + 5b + 10c + 25d + 50e = n
  # 5 is 2
  # 10 is 4
  # 5 + 5, a=5, b=1
  # 10, b=2
  # 10, a=10
  # 10, c=1
  if not cache:
    cache = {i: 0 for i in range(amount+1)}
  
  cache[0] = 1

  for coin in denominations:
    for h_amount in range(coin, amount+1):
      difference = h_amount - coin
      print(difference)
      print(cache)
      cache[h_amount] += cache[difference]
    
  return cache[amount]

# print(making_change(6))

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")