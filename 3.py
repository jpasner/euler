# Project Description
#     The prime factors of 13195 are 5, 7, 13 and 29.
#
#     What is the largest prime factor of the number 600851475143 ?

# Solution: Recusive function which checks to see if input number has any factors and returns the largest prime factor it finds

import math

def is_factor(numerator,divisor):
  if numerator % divisor is 0:
    return 1
  else:
    return 0

def find_prime_factors(number):
  factors_list = []
  i = 2

  upper_limit = number/2

  while i < upper_limit + 1:
    if is_factor(number,i):
      if find_prime_factors(i) > 0:
        # i is a factor, but not prime.  Reset upper limit and continue searching
        upper_limit = number / i
      else:
        # i is a prime factor, continue searching until upper limit is reached.
        factors_list.append(i)
    i += 1

  if not factors_list:
    # number is prime
    return 0
  else:
    # return list of prime factors of number
    return factors_list

big_number = 600851475143

output = find_prime_factors(big_number)

if not output:
  print str(big_number) + " is a prime number"
else:
  print "The prime factors of " + str(big_number) + " are:"
  print output

