# Precedência operadores:
# 1. (n + n)
# 2. **
# 3. *  /  //  %
# 4. + -
# 5. <  >  <=  >=  ==  !=
# 6. and  or  not

conta_1 = (1 + 1) ** (5 + 5)
print(conta_1) # 1024

conta_2 = 1 + 1 ** 5 + 5 
print(conta_2) # 7 (1**5 = 1+5 = 6+1 = 7)

conta_3 = (1 + (0.5 + 0.5)) ** (5 + 5)
print(conta_3) # 1024.0

conta_4 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_4) # 1024 (int(0.5 + 0.5) = 1