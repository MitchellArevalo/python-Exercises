def sumNonPrime(number):
  if (type(number) != int or number < 2):
    return -1
  else:
    resultado = 0
    for i in range(2, number+1):
      primo = True
      for j in range(2, i):
        if i % j == 0:
          primo = False
          break
      
      if (primo == False):
        resultado += i
        print(f"{i} No es primo")
      else:
          print(f"{i} Es Primo")
    return resultado
