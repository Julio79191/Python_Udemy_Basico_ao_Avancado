# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# numeros e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão
nome_completo = 'Canela Seca da Silva' #bom nome de variável
print(nome_completo, type(nome_completo), sep=' - ') 

soma_dois_mais_dois = 2 + 2 #bom nome de variável
print(soma_dois_mais_dois, type(soma_dois_mais_dois), sep=' - ')

int_um = bool('1') #nome ruim de variavel, mas só para exemplificar
print(int_um, type(int_um), sep=' - ')

print( )
nome = 'Julio'
idade = 20
altura = 1.80
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade', idade, 'Altura', altura, "\n" 'Respectivamente:', type(nome), type(idade), type(altura), sep=' - ')

if maior_de_idade:
    print('É maior de idade:', maior_de_idade, type(maior_de_idade), sep=' - ')
else:
    print('É menor de idade:', maior_de_idade,type(maior_de_idade), sep=' - ')

# if - else (se - senão).