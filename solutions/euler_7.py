#!/usr/bin/env python

import sys
import numbertheory.primes

def euler_7(n):
  for i, p in enumerate(numbertheory.primes.postponed_sieve()):
    if i == n - 1: break
  return p


def main():
  n = 10001
  n_prime = euler_7(n)

  print "The %d prime is %d." % (n, n_prime)


if __name__ == "__main__":
  sys.exit(main())