def linkhijo (nodoPadre, nodoHijoiz=None , nodoHijoDer=None):
    if nodoHijoiz is not None :
        nodoPadre.izq =nodoHijoiz
    if nodoHijoDer is not None:
        nodoPadre.der=nodoHijoDer
    pass


def LVR (nodo,inOrderArr):
  ##  nodoHijo=None

#if nodoPadre.izq is not None:
      # nodoHijo= nodoPadre.izq
      #   pass

    #inOrderArr.append(nodoPadre.valor)

    #if nodoPadre.der is not None:
     #    inOrderArr.append(nodoHijo.valor)
    if nodo is not None:
        nodoPadre=nodo
        LVR(nodoPadre.izq,inOrderArr)
        inOrderArr.append(nodoPadre.valor)
        LVR(nodoPadre.der,inOrderArr)

    return inOrderArr 
    