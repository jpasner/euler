# Project Description
#     The prime factors of 13195 are 5, 7, 13 and 29.
#
#     What is the largest prime factor of the number 600851475143 ?

def find_factor(number)
  

big_num = 600851475143
half = 300425737572
factors_list = []
i = 1



while i < 300425737572:
  if big_num % i is 0:
    factors_list.append(i)
  i += 1

print factors_list
