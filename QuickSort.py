def quick_sort(valores, p=0, r=None):
    if r is None:
        r = len(valores) - 1

    if p < r:
        q = particionar(valores, p, r)
        quick_sort(valores, p, q - 1)
        quick_sort(valores, q + 1, r)


def particionar(valores, inicio, fim):
    pivot = valores[fim]
    i = inicio

    for j in range(inicio, fim):
        if valores[j] <= pivot:
            valores[i], valores[j] = valores[j], valores[i]
            i += 1

    valores[i], valores[fim] = valores[fim], valores[i]

    return i


lista = [4, 7, 2, 6, 4, 1, 8, 3]
quick_sort(lista)
print(lista)
