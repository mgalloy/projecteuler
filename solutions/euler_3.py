#!/usr/bin/env python

import math
import sys

import numbertheory.primes


def euler_3(value):
  largest_factor = 1

  for x in numbertheory.primes.postponed_sieve():
    if x > math.sqrt(value): break
    if value % x == 0: largest_factor = x

  return largest_factor

def main():
  value = 600851475143
  largest_factor = euler_3(value)

  print "The largest prime factor of %d is %d." % (value, largest_factor)


if __name__ == "__main__":
  sys.exit(main())

    