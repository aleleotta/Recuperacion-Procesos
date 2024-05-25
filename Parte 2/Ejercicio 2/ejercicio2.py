from multiprocessing import Process, Pipe
from multiprocessing.connection import PipeConnection
from random import randint

def crearRutas(sender: PipeConnection):
    listadoRutas = []
    for i in range(0, 11):
        primerOcteto = randint(0,255)
        ip: str = f"{primerOcteto}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}"
        tuple = (primerOcteto, ip)
        listadoRutas.append(tuple)
    sender.send(listadoRutas)

def clasificarRutas(receiver: PipeConnection, sender: PipeConnection):
    listadoRutas = receiver.recv()
    listadoRutasABC = []
    for tuple in listadoRutas:
        primerOcteto = tuple[0]
        if primerOcteto <= 127: #Class A
            tupleWithClass = (tuple[0], tuple[1], "Class A") #Se agrega un cadena con la clasificacion del ip.
            listadoRutasABC.append(tupleWithClass)
        elif primerOcteto >= 128 and primerOcteto <= 191: #Class B
            tupleWithClass = (tuple[0], tuple[1], "Class B")
            listadoRutasABC.append(tupleWithClass)
        elif primerOcteto >= 192 and primerOcteto <= 223: #Class C
            tupleWithClass = (tuple[0], tuple[1], "Class C")
            listadoRutasABC.append(tupleWithClass)
    sender.send(listadoRutasABC)
    

if __name__ == "__main__":
    left, right = Pipe()
    left1, right1 = Pipe()