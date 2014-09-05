#!/usr/bin/env python

import sys

import numbertheory.fibonacci


def euler_2(limit):
  fib_sum = 0

  for x in numbertheory.fibonacci.generate_fibonacci():
    if x > limit: break
    else:
      if x % 2 == 0: fib_sum += x

  return fib_sum

def main():
  limit = 4000000
  fib_sum = euler_2(limit)

  print "The sum of the Fibonacci numbers less than %d is %d." % (limit, fib_sum)


if __name__ == "__main__":
  sys.exit(main())
