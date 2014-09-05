#!/usr/bin/env python

import sys

import numbertheory.primes

def euler_10(limit):
  s = 0
  for p in numbertheory.primes.postponed_sieve():
    if p >= limit:
      break
    s += p
  return s

def main():
  limit = 2000000   # 2 million
  s = euler_10(limit)
  print "Sum of primes less than %d is %d" % (limit, s)


if __name__ == "__main__":
  sys.exit(main())
