#!/usr/bin/env python

import sys


def euler_9(n):
  for a in xrange(n):
    for b in xrange(a + 1, n):
      if n**2 - 2 * n * (a + b) + 2 * a * b == 0:
        c = 1000 - a - b
        if c > b and c < n:
          return a * b * c, a, b, c

def main():
  n = 1000
  prod, a, b, c = euler_9(n)
  print "Product of Pythagorean triplet is %d, triplet is (%d, %d, %d)" % (prod, a, b, c)


if __name__ == "__main__":
  sys.exit(main())