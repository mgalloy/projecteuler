#!/usr/bin/env python

import numbertheory.primes
import math

if __name__ == "__main__":
  value = 600851475143
  largest_factor = 1

  for x in numbertheory.primes.postponed_sieve():
    if x > math.sqrt(value): break
    if value % x == 0: largest_factor = x

  print "The largest prime factor of %d is %d." % (value, largest_factor)

    