#!/usr/bin/env python

if __name__ == "__main__":
  limit = 1000
  sum = 0

  for x in range(limit):
    if (x % 3 == 0 or x % 5 == 0):
      sum += x

  print "The sum of the multiples of 3 and 5 below %d is %d." % (limit, sum)
    