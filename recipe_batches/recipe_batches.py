#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  count = 0
  baking = True
  while baking:
    for i in recipe:
      if len(recipe) != len(ingredients):
        baking = False
        return count
      elif ingredients[i] < recipe[i]:
        baking = False
        return count
      else:
        ingredients[i] -= recipe[i]
    count +=1

  pass 

#print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))