#!/usr/bin/env python

import sys


def main():
  n = 1000
  for a in range(n):
    for b in range(a + 1, n):
      if n**2 - 2 * n * (a + b) + 2 * a * b == 0:
        c = 1000 - a - b
        if c > b and c < n:
          print "Product of Pythagorean triplet is %d, triplet is (%d, %d, %d)" % (a * b * c, a, b, c)


if __name__ == "__main__":
  sys.exit(main())