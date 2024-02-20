from libs import *
inOrderArr=[]

nodo1 =nodo(1)
nodo2=nodo(2)
nodo3= nodo(3)
nodo4= nodo(4)
nodo5= nodo(5)
nodo6= nodo(6)
nodo7= nodo(7)




linkhijo(nodo1,nodo2,nodo3)
linkhijo(nodo2,nodo4,nodo5)
linkhijo(nodo3,nodo6,nodo7)

LVR(nodo2,inOrderArr)

print (inOrderArr)

print ( nodo1.getArbol())