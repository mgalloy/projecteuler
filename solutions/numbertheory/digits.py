def digits(n):
  return [int(x) for x in list(str(n))]

def value(digits):
  return int(''.join([str(x) for x in digits]))

def is_palindrome(n):
  d = digits(n)
  for x in xrange(len(d) / 2):
    if d[x] != d[- x - 1]: return False
  return True

def reverse(n):
  return value(list(reversed(digits(n))))
  