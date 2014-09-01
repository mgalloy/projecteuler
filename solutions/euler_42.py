#!/usr/bin/env python

import sys
import csv

triangular_values = {}


def is_triangular_word(w):
  s = sum([ord(letter) - 64 for letter in w])
  return s in triangular_values

def main():
  words = []
  filename = 'solutions/p042_words.txt'
  with open(filename, 'r') as words_file:
    csv_reader = csv.reader(words_file)
    for row in csv_reader:
      words.extend(row)

  max_length = max([len(w) for w in words])
  tn = 1
  n = 1
  while tn < max_length * 26:
    triangular_values[tn] = True
    n += 1
    tn = n * (n + 1) / 2

  n_triangular = 0
  for w in words:
    if is_triangular_word(w):
      n_triangular += 1

  print 'There are %d triangular words in %s.' % (n_triangular, filename)


if __name__ == "__main__":
  sys.exit(main())
