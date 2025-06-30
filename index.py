# lista = [1, 3, 5, 7, 8, 0, 2, 4, 6, 8]
# # Coloque os elementos em ordem crescente

# def bubbleshot(lista):
#     for passnum in range(len(lista)-1, 0, -1):
#         for i in range(passnum):
#             if lista[i] > lista[i+1]: 
#                 temp = lista[i]
#                 lista[i] = lista[i+1]
#                 lista[i+1] = temp

# bubbleshot(lista)
# print ("A lista em ordem é:\n", lista)

lista = [1, 3, 5, 7, 8, 0, 2, 4, 6, 8]
a = (len(lista))

while a > 0:
    maior = lista[0]
    for i in range(0, a):
        if maior < lista[i]:
            maior = lista[i]
    lista.remove(maior)
    lista.append(maior)
    a = a - 1
lista.reverse()
print(lista)