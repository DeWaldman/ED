# FUNCOES RECURSIVAS EM PAITO

def inv(s): # inverte um string, recursivamente; o mesmo que s[::-1]
    if len(s) == 0: return s
	return inv(s[1:])+s[0]

def anagrama(s1, s2): #funcao anagrama
	return sorted(s1) == sorted(s2)

def anagrama(s1, s2): #minha versao do anagrama
	return set(s1) == set(s2) and len(s1) == len(s2)
	
def fat(n): #funcao fatorial
	if n==1:return 1
	return n*fat(n-1)
	

def pot(a,b): #funcao potencia
	if b == 1: return a
	return a*pot(a,b-1)
	
def sd(n): # soma os digitos de um numero
	if n <= 9: return n
	return n%10 + sd(n // 10)
	
def mdc(a,b): #funcao mdc
	if a%b == 0: return b
	return mdc(a%b, b = a)
	
def fib(n): #funcao fibonacci usando dict
	f = {}
	if n <=2: return 1
	if n not in f:
		f[n] = fib(n-1)+fib(n-2)
	return f[n]
	


#funcao fibonacci usando o cache do computador pra gardar os valores ja processados
from functools import lru_cache
@lru_cache(maxsize=None)	
def fib(n): #funcao fibonacci usando lru_cache
	if n <=2: return 1
	return f[n] = fib(n-1)+fib(n-2)
"""
@ --> decorador é um recurso avançado de linguagens, onde você faz um "envelope"
da sua função , dando super poderes para ela
"""
