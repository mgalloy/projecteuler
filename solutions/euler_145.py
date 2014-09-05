#!/usr/bin/env python

import sys
import numbertheory.digits


def all_odd_digits(n):
  digits = numbertheory.digits.digits(n)
  for d in digits:
    if d % 2 == 0: return False
  return True

def main():
  # n = 1000   # 1 thousand, result should be 120
  n = 1000000000   # 1 billion
  n_reversible = 0

  for i in xrange(n):
    if i % 1000000 == 0: print i
    if all_odd_digits(i + numbertheory.digits.reverse(i)) and i % 10 != 0:
      n_reversible += 1

  print 'There are %d reversible numbers below %d.' % (n_reversible, n)


if __name__ == "__main__":
  sys.exit(main())