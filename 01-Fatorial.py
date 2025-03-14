def fatorial(number):
    resultado = 1
    while number > 0:
        resultado *= number 
        number -= 1  
    return resultado  


print(fatorial(8))