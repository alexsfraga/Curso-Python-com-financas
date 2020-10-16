# CONDICIONAL   " IF "
if 5 == 15/3:
        print("Hooray !")

if 5 == 18/3:
        print("Hooray !")

# CONDICIONAL   " ELSE "
x=1
if x > 3:
        print("case 1")
else:
        print("case 2")

#CONDICAO   " ELIF "
def com_five(y):
        if y > 5:
                return y,'_ Garden'
        elif y < 0:
                return y,"_ Negativo"
        elif y < 5:
                return y,"_ Less"
        else:
                return y,"_ Equal"

print(com_five(-3))

print(com_five(10))

print(com_five(2))

print(com_five(5))

# VALORES BOOLEANOS
x=2
if x > 4:
        print("Correct")
else:
        print("Incorrect")