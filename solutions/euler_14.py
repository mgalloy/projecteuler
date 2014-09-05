#!/usr/bin/env python

import sys

def collatz(n):
  if n % 2 == 0:
    return n / 2
  else:
    return 3 * n + 1

def collatz_sequence_length(n):
  length = 1
  while n > 1:
    n = collatz(n)
    length += 1
  return length

def euler_14(limit):
  max_len = 0
  max_n = 0
  for n in xrange(limit):
    length = collatz_sequence_length(n)
    if length > max_len:
      max_len = length
      max_n = n
  return max_n, max_len

def main():
  limit = 1000000   # 1 million
  max_n, max_len = euler_14(limit)
  print "Max length of Collatz sequence for values under %d is %d (%d terms)" % (limit, max_n, max_len)

if __name__ == "__main__":
  sys.exit(main())
