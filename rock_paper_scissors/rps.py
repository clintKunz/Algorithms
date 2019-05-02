#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  answer = []
  options = ['r', 'p', 's']
  if n == 0:
    return []
  if n == 1:
    return options

  else:   
    rps = rock_paper_scissors(n-1)
    for i in range(0, 3):
      for j in range(0, 3**(n-1)):
        answer += [options[i] + rps[j]]

  return answer

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

# def rock_paper_scissors_iterative(n):
#   output = []
#   possible_plays = ['scissors', 'paper', 'rock']

#   stack = []
#   stack.append([])

#   while len(stack) > 0:
#     hand = stack.pop()

#     if n == 0 or len(hand) == n:
#       output.append(hand)
#     else:
#       for play in possible_plays:
#         stack.append(hand + [play])

#   return output

# def rock_paper_scissors_recursive(n):
#   outcomes = []
#   plays = ['rock', 'paper', 'scissors']

#   def find_outcome(rounds_left, result=[]):
#     if rounds_left == 0:
#       outcomes.append(result)
#       return
#     for play in plays:
#       find_outcome(rounds_left - 1, result + [play])

#   find_outcome(n, [])
#   return outcomes