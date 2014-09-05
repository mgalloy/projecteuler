#!/usr/bin/env python

import sys

import numbertheory.digits
import numbertheory.operations


def euler_20(n):
  return sum(numbertheory.digits.digits(numbertheory.operations.factorial(n)))

def main():
  n = 100
  s = euler_20(n)
  print 'Sum of the digits of %d! is %d' % (n, s)


if __name__ == "__main__":
  sys.exit(main())
