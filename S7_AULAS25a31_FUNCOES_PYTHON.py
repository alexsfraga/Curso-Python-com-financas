# FUNÇÕES EM PYTHON
#Aula 25
def simples():
    print("My first function")
#simples()

#Aula 26
def plus_ten(a):
    return a+10
x = plus_ten(3)
#print(x)

# aula 27 outra maneira de definir uma funcao
def plus_ten(a):
    result = a+10
    return result
x = plus_ten(3)
#print(x)

#Aula 28 funcao em outra funcao
def wage(w_hours):
    return w_hours  * 25
def with_bonus(w_hours):
    return wage(w_hours) + 50
#print(wage(8), with_bonus(8))

# exercicio da aula 28:
# definir uma funcao que adicione 5 ao parametro.
# Entao definir outra funcao que ira multiplicar o novo dado recebido
# como parametro por 3
def func1(p1):
    return p1+5
def func2(p2):
    return p2*3
#print(func2(func1(5)))

#Aula 29  Combinação
def add_10(m):
    if m >= 100:
        m=m+10
        return m
    else:
        return "Save more !"
#print(add_10(100))

#Aula 30
def sub(a,b,c):
    result = a - b * c
    print("parameter a equals ", a)
    print("parameter b equals ", b)
    print("parameter c equals ", c)
    return result
#print("resultado = ",sub(10,3,2))
#print("resultado = ",sub(c=2,a=10,b=3))

#Aula 31 funções nativas no python
print( type(10) ) # retorna o tipo de variavel, neste caso retorna class int
print( int(5.0) )
print( float(3) )
print( str(500) )
print( max(10,20,30) )
print( min(10,20,30) )

z=-20
print( abs(z) )

list1 = [1,2,3,4]
print( sum(list1) )

print( round(3.555,2) )
print( round(3.2) )

print( 2**10 )
#ou
print( pow(2,10) )

print( len("mathematics") )