l1 = [1,2,2,2,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
l2 = [6,6,6,6,7,7,8,8,8,9,10]

l3 = l1 + l2

# Remover valores repetidos e mostrar lista final
lista_sem_repeticao = list(set(l3))
lista_final = sorted(lista_sem_repeticao)
print("Lista final sem repetição:", lista_final)