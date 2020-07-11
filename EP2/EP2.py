
#______________________M E R L I N______________________
def enumerações(items):
  n = len(items)
  s = [0]*(n+1)
  k = 0
  while True:
    if s[k] < n:
      s[k+1] = s[k] + 1
      k += 1
    else:
      s[k-1] += 1
      k -= 1
    if k == 0: break
    else:
      lista = []
      for j in range(1, k+1):
        lista.append(items[s[j]-1])
      yield lista

def combinações(items, n):
  if n==0: yield []
  else:
    for i in range(len(items)):
      for cc in combinações(items[:i]+items[i+1:],n-1):
        yield [items[i]]+cc

def permutações(items):
  return combinações(items, len(items))


#______________________D A D O S______________________
def pega_dados(file_name: str):
  dados = {}  #retorna um dict
  with open(file_name) as file:
    txt = file.read()

  txt = txt.split('\n')
  for linha in txt:
    nomes = linha.split()
    dados[nomes[0]] = nomes[1:]
  return dados


#______________________I N F O M A C A O______________________
def informacao(dados: dict):
  lista = []
  for key in dados.keys():
    lista.extend(dados[key])
  return set(lista), list(dados.keys()), dados


#______________________S T A R T______________________
def start():
  

  #         Verificando o caso das damas
  print()
  print('Verificando o caso das damas')
  casamentos_files = ('casamento.txt', 'casamento no.txt')
  for file in  casamentos_files:
    print()
    print('Nome do arquivo: ', file)
    queridos, damas, dados = informacao(pega_dados(file))
    if len(queridos) >= len(damas):
      print('É possivel casar todas as damas.')
    else:
      print('Não é possível casar todas as damas.')
      print('Motivo: ', dados)
    print()


  #         Verificando o caso dos cavaleiros  
  print()
  print('Verificando o caso dos cavaleiros')
  cavaleiros_files = ('cavaleiros.txt', 'cavaleiros no.txt')
  for file in  cavaleiros_files:
    print()
    fag = True
    print('Nome do arquivo: ', file)
    IGNORE, cavaleiros, dados = informacao(pega_dados(file))
    for c in permutações(cavaleiros):
      if ( (c[1] in dados[c[0]]) and (c[2] in dados[c[1]]) and (c[3] in dados[c[2]]) and (c[4] in dados[c[3]]) and
           (c[5] in dados[c[4]]) and (c[6] in dados[c[5]]) and (c[0] in dados[c[6]]) ):
        print('encontrado -> ',c)
        fag = False
    
    if fag:
      print('Sem combinacao possivel')




if __name__ == "__main__":
  start()
    

