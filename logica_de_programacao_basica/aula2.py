# sep = separador entre os valores
# end = final da linha
# \r\n -> CRLF (Carriage Return + Line Feed) (quebra de linha no Windows)
# \n -> LF (Line Feed) (quebra de linha no Linux/Mac)
print(12, 34, sep='-', end=' hello')
print(56, 78, sep='', end=' hello again\n')
print(91, 23, sep="hello", end=' ops, wrong space\n')

