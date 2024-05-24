def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1


def achar_menor_indice(lista):
    menor = lista[0]
    indice_menor = 0
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
    return indice_menor


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(pesquisa_binaria(array, 9))