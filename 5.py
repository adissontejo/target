a = input('Insira sua string: ')
b = ''

for i in range(1, len(a) + 1):
  b = b + a[len(a) - i]

print('String invertida:', b)
