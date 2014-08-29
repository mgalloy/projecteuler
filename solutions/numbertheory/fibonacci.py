def generate_fibonacci():
  '''Generator for the Fibonacci sequence.'''
  a = 0
  b = 1
  yield a
  yield b
  while True:
    a, b = b, a + b
    yield b

    