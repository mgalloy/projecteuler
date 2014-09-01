#!/usr/bin/env python

import sys
import numbertheory.digits
import numbertheory.operations


def main():
  n = 100
  s = sum(numbertheory.digits.digits(numbertheory.operations.factorial(n)))
  print 'Sum of the digits of %d! is %d' % (n, s)


if __name__ == "__main__":
  sys.exit(main())
