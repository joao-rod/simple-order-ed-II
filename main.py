from time import sleep

from src.registros import set_register
from src.selecao import select
from src.insercao import insert

print('Para iniciar a aplicação preencha os dados abaixo:')
# A variável recebe os dados de registro como uma tupla
# A escolha da tupla se dá pelo fato de que as tuplas são imutáveis
# E a variável abaixo não pode ser modificada pois será usada em mais de uma função
registros = tuple(set_register())

while True:
  print()
  print('Digite a opção desejada...')
  print('-' * 45)
  print('1 ------- Mostrar dados usando Selection Sort')
  print('2 ------- Mostrar dados usando Insertion Sort')
  print('3 ------- Cadastrar novos registros de livros')
  print('4 ------- Finalizar a aplicação')
  print('-' * 45)
  option = input()

  if option == '1':
    print('ORDENAÇÃO POR SELEÇÃO')
    print(f'Lista não ordenada:\t{list(registros)}')
    print(f'Lista ordenada:\t\t{select(registros)}')
    input('\nClique Enter para ir ao menu...')

  elif option == '2':
    print('ORDENAÇÃO POR INSERÇÃO')
    print(f'Lista não ordenada:\t{list(registros)}')
    print(f'Lista ordenada:\t\t{insert(registros)}')
    input('\nClique Enter para ir ao menu...')

  elif option == '3':
    print('Ao cadastrar novos dados, a lista anterior será perdida.')
    stop = input('Deseja refazer o cadastro? [s / n]: ')
    if stop == 's':
      print('Ok, vamos lá...')
      registros = set_register()
    else:
      print('Ok, os dados atuais foram mantidos.')
      print(f'A lista a ser trabalhada é:\t{list(registros)}')
      print()
      input('Clique Enter para voltar ao menu...')

  elif option == '4':
    print('Você escolheu sair...')
    sleep(0.85)
    break
  
  else:
    print('Digite um valor válido!!')
