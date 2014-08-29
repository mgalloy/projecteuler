#!/usr/bin/env python

import sys
import math


def digits(n):
  n_digits = int(math.ceil(math.log10(n)))
  digits = []
  for x in range(n_digits):
    d = (n % 10 ** (x + 1)) / 10 ** x
    digits.insert(0, d)
  return digits

def is_palindrome(n):
  d = digits(n)
  for x in range(len(d) / 2):
    if d[x] != d[- x - 1]: return False
  return True


def main():
  '''A palindromic number reads the same both ways. The largest palindrome made
     from the product of two 2-digit numbers is 9009 = 91 x 99.

     Find the largest palindrome made from the product of two 3-digit numbers.'''
  largest_palindrome = 1

  for x in range(100, 999):
    for y in range(100, 999):
      n = x * y
      if is_palindrome(n) and n > largest_palindrome:
        largest_palindrome = n

  print "The largest palindrome made from the product of two 3-digit numbers is %d" % largest_palindrome


if __name__ == "__main__":
  sys.exit(main())