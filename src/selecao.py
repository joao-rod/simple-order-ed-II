def select(lista):
  # Transformo a nossa tupla em lista pois ela precisa ser modificada
  aux_list = list(lista)

  for i in range(len(aux_list)):
    # Menor elemento do vetor.
    minimo = i
    for j in range(i + 1, len(aux_list)):
      if aux_list[minimo] > aux_list[j]:
        minimo = j
    # Realoca o elemento mínimo na posição correta.
    aux_list[i], aux_list[minimo] = aux_list[minimo], aux_list[i]
    
  return aux_list
