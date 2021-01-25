# AULA 32 alterando elementos e Deletando
participants = ['john','leila','gregory','cate']
print( participants )
print( participants[1] )
print( participants[-2] )

participants[3] = 'Maria'
print(participants)

del participants[2]
print(participants)

#Aula 33 adicionando elementos na lista
participants.append('Dwayne')
print(participants)

participants.extend(['George','Catherine'])
print(participants)

print("The first participant is "+ participants[0] + ".")
print( len('Dolphin') )
print( len(participants) )

#Aula 34 fatiamento da lista
print(participants[1:3])
print(participants[:2])
print(participants[4:])
print(participants[-2:])

print( participants.index('Maria'))

newcomers = ['Joshua','Brittany']
print(newcomers)
big_list = [participants, newcomers]
print(big_list)
big_list.sort()
print(big_list)

participants.sort()
print(participants)

participants.sort(reverse=True)
print(participants)

numbe1 = [4,5,1,2,6,3]
numbe1.sort()
print(numbe1)
numbe1.sort(reverse=True)
print(numbe1)

#Aula 35  Tuplas tipo de dado direfente da lista
# tuplas fica entre parenteses() e não entre colchetes[]
# não pode acrescentar ou excluir elementos
# a tupla é o tipo de sequencia padrão do Python
x=(40,41,42)
print(x)

y=50,51,52
print(y)

a,b,c=1,4,6
print(c)

print(x[0])

list2 = [x,y]
print(list2)

list2.sort()
print(list2)

(age, y_school) = "30,17".split(',')
print(age)
print(y_school)

def f_info(x):
    a = x**2
    p= 4 * x
    print("Area and Perimeter : ")
    return a,p
print(f_info(3))

#Aula 36  dicionarios
dict = {'k1':"cat",'k2':"dog",'k3':"mouse",'k4':"fish"}
print(dict['k1'])

dict['k5']="parrot"
print(dict)

dict['k2']="squirrel"
print(dict)

# adicionando uma lista no segundo elemento
dep_w = {'dep_1':"peter",'dep_2':["jenifer","michael","tommy"]}
print(dep_w['dep_2'])

team={}
print(team)
team['point guard']="dirk"
team['shooting guard']="al"
team["small forward"]="sean"
team["power forward"]="alexander"
team["center"]="hector"

print(team)

print(team["small forward"])
#retorna "None" quando esta vazio ou nulo ou quando não encontrado
print( team.get("olga") )
print( team.get("center") )

