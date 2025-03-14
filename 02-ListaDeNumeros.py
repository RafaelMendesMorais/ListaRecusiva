def soma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + soma_recursiva(lista[1:])

lista_com_numeros = [1,4,5,2]

print(soma_recursiva(lista_com_numeros))