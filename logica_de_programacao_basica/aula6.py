# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo de dado em outro
# tipos imutáveis e primitivos
# str, int, float, bool
print(int('1'), type(int('1')))  
print(type(float('1') + 1))
print(bool(''))  # string vazia é False
print(bool(' '))  # string com espaço é True
print(str(11) + 'b')
print('a' + 'b', type('a'), sep=' - ')
print(10, type(10), sep=' - ') 
print(11 + 10.0)  # int + float -> float
print(type(11 + 10.0))