n = int(input(''))

n1 = 0
n2 = 1
aux = 0

while aux < n:
  if aux == n-1 :
    print(n1)
  
  else:
    print(n1, end=' ')
  
  n1, n2 = n2, n1 + n2
  aux += 1