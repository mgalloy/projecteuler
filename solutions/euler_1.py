#!/usr/bin/env python

import sys


def euler_1(limit):
  s = 0

  for x in xrange(limit):
    if (x % 3 == 0 or x % 5 == 0):
      s += x

  return s

def main():
  limit = 1000
  s = euler_1(limit)

  print "The sum of the multiples of 3 and 5 below %d is %d." % (limit, s)


if __name__ == "__main__":
  sys.exit(main())
    