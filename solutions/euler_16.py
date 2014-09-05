#!/usr/bin/env python

import sys
import numbertheory.digits


def euler_16(power):
  result = 2 ** power
  digits = numbertheory.digits.digits(result)
  digit_sum = sum(digits)
  return digit_sum

def main():
  power = 1000
  digit_sum = euler_16(power)
  print "The sum of the digits of 2^%d is %s" % (power, digit_sum)


if __name__ == "__main__":
  sys.exit(main())
