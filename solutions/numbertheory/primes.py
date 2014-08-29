def postponed_sieve():
  '''Postponed sieve, by Will Ness
     Original code David Eppstein, ActiveState Recipe 2002

     http://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python
  '''

  def add(D, x, step):
    while x in D: x += step
    D[x] = step

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
