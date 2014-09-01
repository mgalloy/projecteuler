#!/usr/bin/env python

import sys
import numbertheory.operations


def main():
  max_n = 1000000
  str = ''.join([str(x) for x in xrange(1, max_n)])
  digits = [str[0], str[9], str[99], str[999], str[9999], str[99999], str[999999]]
  s = numbertheory.operations.product([int(x) for x in digits])
  print 'The product of the digits d[1], d[10], d[100], ... d[10000000] is %d' % s

if __name__ == "__main__":
  sys.exit(main())
