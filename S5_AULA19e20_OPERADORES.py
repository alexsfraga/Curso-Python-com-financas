# AULA 20 - OPERADORES LOGICOS E DE IDENTIDADE
print('--aula 20 -------------------------------------------------------')
v1 = True
v2 = True
print(v1, 'e', v2, ' = ', v1 and v2)

v1 = True
v2 = False
print(v1, 'e', v2, ' = ', v1 and v2)

v1 = False
v2 = False
print(v1, 'e', v2, ' = ', v1 and v2)

v1 = False
v2 = True
print(v1, 'e', v2, ' = ', v1 and v2)

v1 = not True
print('not True = ', v1)

v1 = not False
print('not False = ', v1)

v1 = 3 > 5
v2 = 10 <= 20
print(v1, 'e', v2, ' = ', v1 and v2)

# orden de importancia dos operadores "NOT" , "AND"  , "OR"
# Acima esta o "NOT"
# em segundo o "AND"
# e em terceiro o "OR"
v1 = True and not True
print('True and not true = ', v1)

v1 = False or not True and True
print('False or not True and True = ', v1)

v1 = True and not True or True
print('True and not True or True = ', v1)

#Operadores de identidade "IS" e "IS NOT"
v1 = 5 is 6
print('5 is 6 = ', v1)

v1 = 5 == 6
print('5 == 6 = ', v1)

v1 = 5 is not 6
print('5 is not 6 = ', v1)

v1 = 5 != 6
print('5 != 6 = ', v1)

print('--aula 19-------------------------------------------------------')
#AULA 19 - OPERADORES DE COMPARAÇÃO
# == NÃO ATRIBUI VALOR MAIS SIM VERIFICA UMA CONDIÇÃO DE IGUALDADE
print(10 == 20/2)
    #true
#  !=  VERIFICA A CONDIÇÃO SE DIFERENTE
print(10 != 10)
   #false
# >  CONDICIONADOR MAIOR QUE
print(100 > 50)
   #true
# <  CONDICIONADOR MENOR QUE
print(100 < 50)
   #false
# >=  CONDICIONADOR MAIOR ou IGUAL
print(15 >= 10 + 10)
   #false
# <=  CONDICIONADOR MENOR ou IGUAL
print(15 <= 10 + 5)
   # true