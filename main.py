from libs import *
inOrderArr=[]
PreOrderArr=[]
PostOrderArr=[]

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
print("Getarbol:")
print ( nodo1.getArbol())

print("--------------------------------------------------------------------------------------")

LVR(nodo1,inOrderArr)
print("InOrder:")
print (inOrderArr)



VLR(nodo1,PreOrderArr)
LRV(nodo1,PostOrderArr)


print ("PreOrder:")
print(PreOrderArr)
print("PostOrder:")
print (PostOrderArr)

print("-------------------------------------------------------------------------------")
arrNodos=[16,5,7,12,9,20,18,3,10,14]
nodoRaiz= None
#nodoRaiz=nodo(16)
#nodo9=nodo(5)
#nodo10=nodo(7)
#nodo11=nodo(12)
#nodo12=nodo(9)
#nodo13=nodo(20)
#nodo14=nodo(18)
#nodo15=nodo(3)
#nodo16=nodo(10)
#nodo17=nodo(14)

for i in range (0,len(arrNodos),1):
    if i == 0 :
        nodoRaiz = nodo (arrNodos[i])
    else:
        nodoOrdenados(nodoRaiz,nodo(arrNodos[i]))
        
pass


  

#nodoOrdenados(nodoRaiz,nodo9)
#nodoOrdenados(nodoRaiz,nodo10)
#nodoOrdenados(nodoRaiz,nodo11)
#odoOrdenados(nodoRaiz,nodo12)
#nodoOrdenados(nodoRaiz,nodo13)
#nodoOrdenados(nodoRaiz,nodo14)
#nodoOrdenados(nodoRaiz,nodo15)
#nodoOrdenados(nodoRaiz,nodo16)
#nodoOrdenados(nodoRaiz,nodo17)


Printarbol(nodoRaiz)
#(nodo9.getArbol())
#print(nodo10.getArbol())
#print(nodo11.getArbol())
#print(nodo12.getArbol())
#print(nodo13.getArbol())
#print(nodo14.getArbol())
#print(nodo15.getArbol())
#print(nodo16.getArbol())
##print(nodo17.getArbol())