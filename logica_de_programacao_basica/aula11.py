# Ordem de Precedência
# 1. (n + n) 
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + 1) ** (5 + 5) #1024
conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1, type(conta_1), sep=' - ', end=print(conta_1))
print(conta_2, type(conta_2), sep=' - ', end=print(conta_2))

