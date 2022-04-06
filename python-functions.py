# def fn
# declare variables
# method, iterate 
# action on variables
# return

# challenge one
# write a function named sum_to that accepts a single integer(n) and returns the sum of the integers from 1 to n

def sum_to(n):
  return sum(range(1, n + 1))

# challenge two
# write a function named largest that takes a list of numbers as an argumenmt and return the largest number in that list

def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest

# challenge three
# write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string

def occurrences(str, str2):
  return str.count(str2)

# challenge four
# write a function named product that takes an arbitrary number of numbers, multiplies them all together and returns the product; review notes on args

def product(*args):
  product = 1
  for arg in args:
    produdct *= arg
  return product

print(product(2, 5, 5))

