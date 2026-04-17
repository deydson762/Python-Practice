tupla = (1, 2, 3, 4, 5)
print(tupla)

# Acessar elementos
print("Primeiro elemento:", tupla[0])
print("Último elemento:", tupla[-1])

# Fatiamento (slicing)
print("Elementos do índice 1 ao 3:", tupla[1:4])
print("Do início ao índice 2:", tupla[:3])

# Concatenar tuplas
tupla2 = (6, 7, 8)
nova_tupla = tupla + tupla2
print("Tupla concatenada:", nova_tupla)

# Repetir tupla
tupla_repetida = tupla * 2
print("Tupla repetida:", tupla_repetida)

# Verificar se elemento existe
print("3 está na tupla?", 3 in tupla)
print("10 está na tupla?", 10 in tupla)

# Contar elementos
print("Quantidade de elementos:", len(tupla))

# Contar ocorrências
tupla_com_repeticao = (1, 2, 2, 3, 2, 4)
print("Quantas vezes o 2 aparece:", tupla_com_repeticao.count(2))

# Encontrar índice de um elemento
print("Índice do elemento 3:", tupla.index(3))

# Desempacotar tupla
a, b, c, d, e = tupla
print("Desempacotado:", a, b, c, d, e)

# Tupla com diferentes tipos
tupla_mista = (1, "texto", 3.14, True)
print("Tupla mista:", tupla_mista)

# Tupla aninhada
tupla_aninhada = ((1, 2), (3, 4), (5, 6))
print("Tupla aninhada:", tupla_aninhada)
print("Primeiro elemento da primeira tupla:", tupla_aninhada[0][0])

# Converter lista para tupla
lista = [10, 20, 30]
tupla_convertida = tuple(lista)
print("Lista convertida para tupla:", tupla_convertida)

# Converter tupla para lista
tupla_para_lista = list(tupla)
print("Tupla convertida para lista:", tupla_para_lista)

# Mínimo e máximo
print("Valor mínimo:", min(tupla))
print("Valor máximo:", max(tupla))
print("Soma dos elementos:", sum(tupla))