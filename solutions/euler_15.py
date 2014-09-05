#!/usr/bin/env python

import sys
import numbertheory.operations as ops

def euler_15(m, n):
  n_routes = ops.factorial(m + n) / ops.factorial(m) / ops.factorial(n)
  return n_routes

def main():
  m = 20
  n = 20
  n_routes = euler_15(m, n)
  print "There are %d routes through a %d x %d grid." % (n_routes, m, n)

if __name__ == "__main__":
  sys.exit(main())
