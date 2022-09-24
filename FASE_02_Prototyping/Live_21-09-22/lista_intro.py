# Criação de listas
lista = []
# Criação de listas com dados
lista = [2005, 2002, 1980, 1977, 1999]
# Exibir lista completa
print(lista)
# Exibição de uma posição especifica na lista
print(lista[3])
# Exibição de intervalos na lista. No indice o primeiro valor significa "a partir de" e o segundo "até"
print(lista[2:4])
# Iteração da lista
for ano in lista:
    print(ano)

# Inclusão de dados na última posição da lista
lista.append(2022)
print(lista)

# Inclusão de dados em um índice específico da lista
lista.insert(0, 3000)
print(lista)

# Remover um elemento específico da lista
lista.pop(2)
print(lista)

# Remover último elementol
lista.pop()
print(lista)

# Remover um valor específico da lista
lista.append(2005)
print(lista)
lista.remove(2005)
print(lista)

# Contar indicências de um elemento
print(lista.count(2005))

# Inversão da lsita
lista.reverse()
print(lista)

# Ordenação da lista
lista.sort()
print(lista)
lista.sort(reverse=True)

# Contagem de elementos da lista
print(len(lista))