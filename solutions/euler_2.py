#!/usr/bin/env python

import numbertheory.fibonacci


if __name__ == "__main__":
  fib_sum = 0
  limit = 4000000

  for x in numbertheory.fibonacci.generate_fibonacci():
    if x > limit: break
    else:
      if x % 2 == 0: fib_sum += x

  print "The sum of the Fibonacci numbers less than %d is %d" % (limit, fib_sum)
