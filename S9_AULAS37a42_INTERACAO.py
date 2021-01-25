# AULA 37 - INTERACAO
# for loop
print(" --- Aula 37 ------------------------------------")
even = [0,2,4,6,8,10,12,14,16,18,20]

for n in even:
    print(n)

# AULA 38  - While
print(" --- Aula 38 ------------------------------------")

x: int=0
while x <= 20:
    print(x)
    x = x+4.99

#Aula 39 - create list with the range() function
#range(start, stop, step)
#start = o primeiro numero na lista
#stop  = o ultimo valor +1
#step  = a distancia a cada dois valores consecutivos
print(" --- Aula 39 ------------------------------------")
#range(0,10,0)
print(list(range(10)))
print(list(range(3,7)))
print(list(range(1,20,2)))
print(list(range(0,20,2)))
print(list(range(-1,20,2)))

#Aula 40 - aplicando na pratica o range()
# em um for loop
print(" --- Aula 40 ------------------------------------")

x=[0,1,2]
for var in x:
    print(var)

print(" -- teste 2 -- ")
for var in range(len(x)):
    print(x[var])

#Aula 41 - instruções condicional contar elementos do objeto
print(" --- Aula 41 ------------------------------------")

def count(param):
    total=0
    for vx in param:
        if vx < 20:
            #print(vx)
            total = total + 1
    return total

lst1=[1,3,7,15,23,43,56,98,17]
#y=count(lst1)
print(count(lst1))

#Aula 42 Iteracao em um Dicionario
print(" --- Aula 42 ------------------------------------")

prices = {
    "box_of_spaghetti":4,
    "lasagna":5,
    "hamburger":2
}
quantity={
    "box_of_spaghetti": 6,
    "lasagna": 10,
    "hamburger": 0
}
#print(list(prices.keys())[i])

var_x = int(input("digite o valor de referencia para busca "))
def func1():
    money_spent = 0
    for i in prices:
        money_spent = money_spent + (prices[i]*quantity[i])
    return money_spent

lst = {"nome":[],"tot":0}
def func2(v_param):
    money_spent = 0
    i=int(0)
    for i in prices:
        product_spent = 0
        if prices[i] <= v_param:
            product_spent = prices[i]*quantity[i]
            money_spent = money_spent + product_spent
            var1 = list(prices)[list(prices).index(i)]
            lst["nome"].append(var1)
    lst["tot"] = money_spent
    #return lst

def func3(p_lst):
    v_ls = p_lst["nome"]
    x = 1
    for i in v_ls:
        print("item ", x ," = ",i)
        x = x+1

print("Total gasto nas compras = ",func1())
func2(var_x)
print("Gastos em produtos <= ",var_x,", total = ", lst["tot"])
func3(lst)

import math
print(math.sqrt(var_x))