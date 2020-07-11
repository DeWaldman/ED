from random import shuffle
from random import choice
import time

#____________________________F U N C O E S  D E  O R D E N A C A O____________________________
def selecao(v):
  r = []
  while v:
    m = min(v)
    r.append(m)
    v.remove(m)
  return r


def insercao(v):
  for j in range(1, len(v)):
    x = v[j]
    i = j - 1
    while i >= 0 and v[i] > x:
      v[i+1] = v[i]
      i = i - 1
    v[i + 1] = x
  return v


def mergesort(v):
  if len(v) <= 1: return v
  else:
    m = len(v) // 2
    e = mergesort(v[:m])
    d = mergesort(v[m:])
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
      if e[i] <= d[j]:
        r.append(e[i])
        i += 1
      else:
        r.append(d[j])
        j += 1
    r += e[i:]
    r += d[j:]
    return r


def quicksort(v):
  if len(v) <= 1: # Pior caso: Se vetor ja estiver ordenado
    return v
  pivô = v[0] 
  iguais  = [x for x in v if x == pivô]
  menores = [x for x in v if x <  pivô]
  maiores = [x for x in v if x >  pivô]
  return quicksort(menores) + iguais + quicksort(maiores)


#____________________________F U N C O E S  D E  B U S C A____________________________
def busca_binaria(v, x):
  e = -1
  d = len(v)
  while e < d-1:
    m = (e + d) // 2
    if v[m] < x:
      e = m
    else:
      d = m
  return d


def busca_sequencial(v, x):
  for i in v:
    if i == x:
      return i
  return -1  


#____________________________F U N C O E S  D E  G E T  T E M P O____________________________
def tempo_de_busca(funcao, lista, n):
  a = time.time()
  funcao(lista, n)
  return time.time() - a


def tempo_de_ordenacao(funcao, lista):
  a = time.time()
  funcao(lista)
  return time.time() - a


#____________________________N U M E R O  D E  B U S C A S____________________________
def buscas(lista_original, funcoes_de_ordenacao):
  tempo_das_funcoes_de_ordenacao = [0,0,0,0,0] 
  lista_de_busca = [0,0,0,0,0]
  i = 0 # <-- indice: representa cada funcao em funcoes_de_ordenacao
  for funcao in funcoes_de_ordenacao:
    quantidade_de_buscas = 0; 
    lista_ordenada = funcao(list(lista_original))

    tempo_seq = tempo_de_busca(busca_sequencial, list(lista_original), choice(lista_original))
    tempo_ord = tempo_de_ordenacao(funcao, list(lista_original))
    tempo_bin = tempo_de_busca(busca_binaria, lista_ordenada, choice(lista_original))

    tempo_das_funcoes_de_ordenacao[i] = tempo_ord

    while (tempo_ord + tempo_bin) > tempo_seq:
      tempo_bin += tempo_de_busca(busca_binaria, lista_ordenada, choice(lista_original))
      tempo_seq += tempo_de_busca(busca_sequencial, lista_original, choice(lista_original))

      quantidade_de_buscas += 1

    lista_de_busca[i] = quantidade_de_buscas

    i += 1
  return tempo_das_funcoes_de_ordenacao, lista_de_busca


#____________________________S T A R T____________________________
def start():
  quantidade_de_elementos = 5000
  lista_original = list(range(1,quantidade_de_elementos)); shuffle(lista_original)
  funcoes_de_ordenacao = [selecao, insercao, mergesort, quicksort, sorted]
  
  tela_incial()
  for loop in range(4):
    tempo_das_funcoes_de_ordenacao, lista_de_busca = buscas(lista_original, funcoes_de_ordenacao)
    
    print(f'|  {quantidade_de_elementos:<6}|   {tempo_das_funcoes_de_ordenacao[0]:<8.2f}   {tempo_das_funcoes_de_ordenacao[1]:<7.2f}   {tempo_das_funcoes_de_ordenacao[2]:<6.2f}   {tempo_das_funcoes_de_ordenacao[3]:<6.2f}   {tempo_das_funcoes_de_ordenacao[4]:<6.3f}   |   {lista_de_busca[0]:<8}   {lista_de_busca[1]:<7}   {lista_de_busca[2]:<6}   {lista_de_busca[3]:<6}   {lista_de_busca[4]:<6}   |')
    print(f'|........|.......................................................................................................|')


    quantidade_de_elementos += 5000
    lista_original = list(range(1,quantidade_de_elementos)); shuffle(lista_original)
    
#____________________________T E L A  I N I C I A L____________________________
def tela_incial():
  print(f"""
 _......................................[EP1 - Vale a pena ordenar?]............................................_
|                                                                                                                |
|                 Aluno: Daniel de Souza Lima Junior  -  Fatec - FATEC Sao Jose dos Campos                       |
|                                     ADS - 3º Semestre B - Estrutura de Dados                                   |
|                                                                                                                |
|                       Tempos de Ordenacao (segundos)                      Numero de Buscas                     |
|----------------------------------------------------------------------------------------------------------------|
|  n     |   Insercao   Selecao   Merge.   Quick.   Sorted   |   Insercao   Selecao   Merge.   Quick.   Sorted   |
|........|.......................................................................................................|""")


start()
