#!/usr/bin/env python

'''2520 is the smallest number that can be divided by each of the numbers from
   1 to 10 without any remainder.

   What is the smallest positive number that is evenly divisible by all of the
   numbers from 1 to 20?
'''

import sys
import numbertheory.primes
import math


def main():
  limit = 20
  value = 1
  for x in numbertheory.primes.postponed_sieve():
    if x > limit: break
    value *= x ** int(math.log(limit) / math.log(x))

  print "The smallest number that is evenly divisble by all numbers 1 to %d is %d." % (limit, value)

if __name__ == "__main__":
  sys.exit(main())