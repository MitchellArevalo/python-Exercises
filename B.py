def measureProduction(n_measures):
    if (not isinstance(n_measures, int) or n_measures < 1):
        return -1
    
    total = 0
    
    for i in range(n_measures):
        while True:
            try:
                peso = float(input(f"Ingrese el peso del lote {i+1}: "))
                if peso < 0:
                    print("Ingrese un número válido.")
                    continue
                total += peso
                break
            except ValueError:
                print("Ingrese un número válido.")
    
    promedio = total / n_measures
    
    measurements = [total, promedio]
    
    return measurements
