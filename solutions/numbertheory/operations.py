def factorial(n):
  f = 1
  for i in xrange(1, n + 1): f *= i
  return f

def product(iter):
  p = 1
  for i in iter: p *= i
  return p
