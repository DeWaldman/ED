matrix = '''
0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110
'''

#_________________B U S C A_________________
def busca(regioes: list, ponto: tuple):
  for w in range(len(regioes)):
    try:
      regioes[w].index(ponto)
      return w
    except:
      continue


#_________________E N T R A D A_________________
def entrada(matrix: str):
  matrix = matrix.split()
  qtd_linhas = len(matrix)
  qtd_colunas = len(matrix[0])
  for a in range(qtd_linhas):
    matrix[a] = list(matrix[a])
  return matrix, qtd_linhas, qtd_colunas


#_________________C R I A C A O_________________
def criacao(matrix: list, qtd_linhas: int, qtd_colunas: int):
  regioes = []
  for a in range(qtd_linhas):
    for b in range(qtd_colunas):
      if matrix[a][b] == '1':
        regioes.append([(a, b)])
        
        x = a-1
        y = b-1
        if x == -1:
          x = 0
        if y == -1:
          y = 0
        
        if not (a == x) and matrix[x][b] == '1':
          r = busca(regioes, (x, b))
          regioes[-1].extend(regioes[r])
          del regioes[r]
        
        if not (b == y) and matrix[a][y] == '1' and (a,y) not in regioes[-1]:
          r = busca(regioes, (a, y))
          regioes[-1].extend(regioes[r])
          del regioes[r]

  return regioes
    

#_________________S A I D A_________________
def saida(matrix: list, regioes: list):
  cont = 1
  for regiao in regioes:
    for ponto in regiao: 
     matrix[ponto[0]][ponto[1]] = str(cont)
    cont+=1
  
  for a in matrix:
    print(''.join(a))



#_________________I N I C I O_________________
matrix, linhas, colunas = entrada(matrix)    
regioes = criacao(matrix, linhas, colunas)   
saida(matrix, regioes)                       



