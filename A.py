def calculateDiff(lista):
    numeros = []
    if type(lista) is not list:
        return False
    
    for n in lista:
        if(type(n)is [int, float]):
            numeros.append(n)
    
    if len(numeros) < 2:
        return False
    
    diferencia = max(numeros) - min(numeros)
    return diferencia
