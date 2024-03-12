def fibonacci(number):
    if (number <= 1):
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2) 

def mainFunction():
    nTerms = int(input("Ingrese número de elementos de la secuencia de Fibonacci: "))
    if nTerms <= 0:
        print("Por favor ingrese un número mayor que cero.")
        mainFunction() 
    else:
        print("Secuencia Fibonacci")
        for i in range(nTerms): 
            print(fibonacci(i), end=" ") 

mainFunction()