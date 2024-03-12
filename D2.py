def saveDivisors(number):
    with open("Divisors.txt", "w") as file:
        for i in range(1, number + 1):
            if number % i == 0:
                file.write(str(i) + "\n")
                
saveDivisors(100)