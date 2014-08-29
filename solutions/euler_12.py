#!/usr/bin/env python


def postponed_sieve():
  '''Postponed sieve, by Will Ness
     Original code David Eppstein, ActiveState Recipe 2002

     http://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python
  '''

  def add(D, x, step):
    while x in D: x += step
    D[x] = step
    print D

  yield 2; yield 3; yield 5; yield 7;    # start with first sequence of primes
  D = {}
  ps = (p for p in postponed_sieve())    # a separate Primes Supply:
  p = ps.next() and ps.next()            # (3) a Prime to add to dict
  q = p * p                              # (9) when its square, q, is
  c = 9                                  # the next Candidate
  while True:
    if c not in D:                 # not a multiple of any prime seen so far:
      if c < q: yield c            #   a prime (if less than p^2), or
      else:   # (c == q):          #   the next prime's square:
        add(D, c + 2 * p, 2 * p)   #     (9 + 6, 6 : 15, 21, 27, 33,...)
        p = ps.next()              #     (5)
        q = p * p                  #     (25)
    else:                          # c is a composite
      s = D.pop(c)                 #   step of increment
      add(D, c + s, s)             #   next multiple, same step
    c += 2

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
