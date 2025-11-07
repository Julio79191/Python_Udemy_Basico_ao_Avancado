'''
tipos int e float
int -> Número inteiro
O tipo int representa qualquer número inteiro,
positivo ou negativo. 
int sem sinal é considerado positivo.
'''
print(11) #int
print(-11) #int
print(0) #int
print(11 , -11, sep='/') #int

"""
float -> Número com ponto flutuante
O tipo float representa qualquer número positivo ou negativo
com ponto flutuante. 
float sem sinal é considerado positivo.
"""
print(1.1) #float
print(-1.5) #float
print(0.0) #float
print(1.1 , -1.5, sep='/') #float

# a função type mostra o tipo que o Python
# inferiu ao valor. 
print(type(11), type(1.1), type(-1.5), type(0), sep='\n')