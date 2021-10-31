def insert(lista):
  # Transformo a tupla em lista pois ela precisa ser modificada
  aux_list = list(lista)
  
  for j in range(1, len(aux_list)):
    chave = aux_list[j]
    i = j - 1
    # Realoca aux_list[j] na posição certa.
    while i >= 0 and aux_list[i] > chave:
      aux_list[i + 1] = aux_list[i]
      i = i - 1
    aux_list[i + 1] = chave

  return aux_list
