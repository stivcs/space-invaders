from io import *
class usuario:
    def __init__(self,nombre,fecha,score):
        self.nombre = nombre
        self.fecha = fecha
        self.score = score
    def getn(self):
        return self.nombre
    def getf(self):
        return self.fecha
    def gets(self):
        return str(self.score)

def guardardatos(date):
    arc = open("datos.txt","a")
    arc.write(f"\n{date.getn()}\t\t{date.getf()}\t\t{date.gets()}")
    arc.close()

def leer():
    arc = open("datos.txt","r")
    lec = arc.read()
    arc.close()
    return lec