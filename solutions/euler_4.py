#!/usr/bin/env python

'''A palindromic number reads the same both ways. The largest palindrome made
   from the product of two 2-digit numbers is 9009 = 91 x 99.

   Find the largest palindrome made from the product of two 3-digit numbers.'''

import sys
import math
import numbertheory.digits


def main():
  largest_palindrome = 1

  for x in xrange(100, 999):
    for y in xrange(100, 999):
      n = x * y
      if numbertheory.digits.is_palindrome(n) and n > largest_palindrome:
        largest_palindrome = n

  print "The largest palindrome made from the product of two 3-digit numbers is %d." % largest_palindrome


if __name__ == "__main__":
  sys.exit(main())