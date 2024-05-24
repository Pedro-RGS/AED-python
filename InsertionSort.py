def insertion_sort(lista):
    tamanho = len(lista)

    for i in range(1, tamanho):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave


lista = [4, 2, 5, 3, -1]
insertion_sort(lista)
print(lista)
