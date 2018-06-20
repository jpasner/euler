# Project description:
#     Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
#     1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#     By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def even(number):
  if number % 2 is 0:
    return 1
  else:
    return 0

fib = [1,2]
total = 2

while fib[1] < 4000000:
  fib.append(fib.pop(0) + fib[0])
  if even(fib[1]):
    total += fib[1]

print total
