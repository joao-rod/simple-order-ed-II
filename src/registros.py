from random import randint
from time import sleep

def set_register():
  n = int(input('\nQuantidade de registros: '))

  # Defino a tamanho "n" do vetor
  registros = [None] * n
  cont = 0

  # Entrada e gravação de dados
  while cont < len(registros):
    nome = str(input('\nNome do livro: '))
    num_livro = int(input(f'Quantos livros "{nome}" devo registrar: '))

    # Escopo que permite que o valor a ser guardado no vetor fique numa posição aleatória
    while True:
      aux = randint(0, n - 1)  
      if registros[aux] == None:
        print(f'Posição sorteada: {aux}')
        registros[aux] = num_livro
        print(f'Valor {num_livro} salvo na posição {aux}')
        cont += 1
        break
      else:
        print(f'Posição sorteada: {aux} - Posição já preenchida. Sorteando novamente uma posição...')
        sleep(1)

  print('Para a atividade, considere a lista com as quantidades de livros.')
  print(f'A lista a ser trabalhada é: {registros}\n')
  sleep(1)
  input('Clique Enter para ir ao menu...')

  return registros
  