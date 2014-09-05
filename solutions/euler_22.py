#!/usr/bin/env python

import sys
import csv


def main():
  names = []
  filename = 'solutions/p022_names.txt'
  with open(filename, 'r') as words_file:
    csv_reader = csv.reader(words_file)
    for row in csv_reader:
      names.extend(row)

  names.sort()

  total_value = 0
  for index, n in enumerate(names):
    s = sum([ord(letter) - 64 for letter in n])
    total_value += (index + 1) * s
    print "%s: %d [%d]" % (n, s, index + 1)

  print "The total of the index times letter sum of the names is %d." % total_value


if __name__ == "__main__":
  sys.exit(main())