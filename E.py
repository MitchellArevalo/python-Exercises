def sumLists(lista1, lista2):
    if type(lista1) is not list or type(lista2) is not list or len(lista1) != len(lista2):
        return -1
    for i in lista1 + lista2:
        if not isinstance(i, (int, float)):
            return -1
    
    Resultados = []
    sum1 = sum(lista1)
    sum2 = sum(lista2)
    for i in range(len(lista1)):
        Resultados.append(lista1[i] + lista2[i])
    
    Resultados.append(sum1 + sum2)
    
    return Resultados
