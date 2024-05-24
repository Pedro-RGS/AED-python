def merge_sort(lista, inicio, fim):
    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)

        merge(lista, inicio, meio, fim)


def merge(lista, inicio, meio, fim):
    esquerdo = lista[inicio:meio]
    direito = lista[meio:fim]
    topoE = 0
    topoD = 0

    for i in range(inicio, fim):
        if topoE >= len(esquerdo):
            lista[i] = direito[topoD]
            topoD += 1
        elif topoD >= len(direito):
            lista[i] = esquerdo[topoE]
            topoE += 1
        elif esquerdo[topoE] < direito[topoD]:
            lista[i] = esquerdo[topoE]
            topoE += 1
        else:
            lista[i] = direito[topoD]
            topoD += 1


lista = [5, -1, 5, 2, 0, 1]
merge_sort(lista, 0, 6)
print(lista)
