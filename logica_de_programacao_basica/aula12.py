nome = 'Julius Costas'
altura = 1.80
peso = 110 # to gordao mané, que isso
imc = peso / (altura * altura)
imc = peso / altura ** 2 #ambos resultados seram identicos

print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'e seu IMC é')
print(imc)