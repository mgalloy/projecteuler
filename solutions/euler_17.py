#!/usr/bin/env python

import sys

words = {}
words[1000] = 'thousand'
words[100] = 'hundred'
words[90] = 'ninety'
words[80] = 'eighty'
words[70] = 'seventy'
words[60] = 'sixty'
words[50] = 'fifty'
words[40] = 'forty'
words[30] = 'thirty'
words[20] = 'twenty'
words[19] = 'nineteen'
words[18] = 'eighteen'
words[17] = 'seventeen'
words[16] = 'sixteen'
words[15] = 'fifteen'
words[14] = 'fourteen'
words[13] = 'thirteen'
words[12] = 'twelve'
words[11] = 'eleven'
words[10] = 'ten'
words[9] = 'nine'
words[8] = 'eight'
words[7] = 'seven'
words[6] = 'six'
words[5] = 'five'
words[4] = 'four'
words[3] = 'three'
words[2] = 'two'
words[1] = 'one'
words[0] = ''

def number_of_letters(n):
  if n == 1000:
    return len(words[1]) + len(words[1000])
  elif n >= 100:
    n_hundreds = n / 100
    r = n % 100
    if r == 0:
      return len(words[n_hundreds]) + len(words[100])
    else:
      return len(words[n_hundreds]) + len(words[100]) + len('and') + number_of_letters(r)
  elif n > 20:
    n_tens = n / 10
    r = n % 10
    return len(words[n_tens * 10]) + len(words[r])
  else:
    return len(words[n])

def euler_17(limit):
  s = 0
  for n in xrange(1, limit + 1):
    s += number_of_letters(n)
  return s

def main():
  limit = 1000
  s = euler_17(limit)
  print "Number of letters for all numbers from 1 to %d is %d" % (limit, s)


if __name__ == "__main__":
  sys.exit(main())
