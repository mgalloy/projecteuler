#!/usr/bin/env python


def triangulars():
  x = 0
  n = 1
  while True:
    x, n = x + n, n + 1
    yield x

def n_divisors(n):
  n_div = 1
  limit = n / 2
  primes = postponed_sieve()
  for p in primes:
    if p > limit: break
    p_expo = 0
    f = n

    while f % p == 0:
      p_expo += 1
      f /= p

    n_div *= p_expo + 1

  return n_div


if __name__ == "__main__":
  i = 0
  max_div = 0
  for x in triangulars():
    n_div = n_divisors(x)

    # provide some feedback
    i += 1
    if n_div > max_div:
      max_div = n_div
      print "triangular[%d] = %d, max_div = %d" % (i, x, max_div)

    if n_div > 500:
      print x
      break
