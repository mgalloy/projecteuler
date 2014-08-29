#!/usr/bin/env python

import sys


def main():
  n = 100
  sum_of_squares = n * (n + 1) * (2 * n + 1) / 6
  square_of_sum = (n * (n + 1) / 2) ** 2
  print "Difference of square of sum and sum of squares of first %d numbers is %d." % (n, square_of_sum - sum_of_squares)


if __name__ == "__main__":
  sys.exit(main())