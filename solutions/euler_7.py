#!/usr/bin/env python

import sys
import numbertheory.primes


def main():
  i = 1
  n = 10001
  for x in numbertheory.primes.postponed_sieve():
    if i == n:
      print "The %d prime is %d" % (n, x)
      break
    i += 1


if __name__ == "__main__":
  sys.exit(main())