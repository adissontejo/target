a = 0
b = 1

n = int(input('Informe o número escolhido: '))

if n == 0:
  print(n, 'pertence a sequência Fibonacci.')
else:
  while b < n:
    x = a + b
    a = b
    b = x

  if b == n:
    print (n, 'pertence a sequência Fibonacci.')
  else:
    print(n, 'não pertence a sequência Fibonacci.')
