
"""sem usar dict ou CACHE e sem usar 2**n"""

def f(n):
    if n == 0: return 1
    return f(n-1)*2 #f(n-1) + f(n-1)

print(f(10))
print("_"*50)

#__________________P O N T E I R O S__________________


lista1 = [1, 2, 3]
lista2 = lista1
lista1[0] = 42
print(lista1)
print(lista2)
print("_"*50)


""" uma copia e nao um ponteiro"""
lista1 = [1, 2, 3]
lista2=list(lista1)
lista1[0] = 42
print(lista1)
print(lista2)
print("_"*50)

"""
Pyhton tem ponteiros, só que eu os uso em alto nível.
Em C manipulo ponteiros em baixo nível.
A memoria pode ser vista como um vetor
gigantesco de bytes, cada índice é o endereço.
Em C char ocupa um byte, int ocupa 4 bytes.

Ponteiros em C acessa váriaveis através do seu endereço,
ou regioes de memória, mesmo que não tenham variáveis declaradas

1) Ponteiro e coisa apontada são duas coisas diferenes
2) Não tem sentido usar um ponteiro que não tenha
sido inicializado, isto é, que não aponte para ninguém

Em C ponteiros são usados para muitas coisas
1) Passagem por referência em funções. Por exemplo: scanf("%d", &n)
2) Posso declarar vetores com tamanho calculando em tempo de execução
int *v;
v pode significar duas coisas, um ponteiro para um único inteiro, ou um vetor
que é alocado em tempo de execucão
#em casa acesse bit.ly/fatecED
#lá tem um link do dropbox do código em C
"""
