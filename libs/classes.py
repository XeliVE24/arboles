class nodo ():
    def __init__(self,valor):
        self.valor = valor
        self.izq = None
        self.der = None 
        pass

    def __str__(self):
        return f"Valor:{self.valor} ,izq:{self.izq} ,der:{self.der}"

pass