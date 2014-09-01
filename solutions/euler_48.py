#!/usr/bin/env python

import sys


def main():
  n = 1000
  s = sum([(i ** i) % (10 ** 10) for i in xrange(1, n + 1)]) % (10 ** 10)

  print "Sum of ith integer to the ith power for the first %d integers is %d." % (n, s)


if __name__ == "__main__":
  sys.exit(main())