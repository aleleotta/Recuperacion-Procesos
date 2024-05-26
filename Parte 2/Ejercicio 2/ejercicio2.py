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
            tupleWithClass = (tuple[1], "Class A") #Se agrega una cadena con la clasificacion del ip.
            listadoRutasABC.append(tupleWithClass)
        elif primerOcteto >= 128 and primerOcteto <= 191: #Class B
            tupleWithClass = (tuple[1], "Class B")
            listadoRutasABC.append(tupleWithClass)
        elif primerOcteto >= 192 and primerOcteto <= 223: #Class C
            tupleWithClass = (tuple[1], "Class C")
            listadoRutasABC.append(tupleWithClass)
    sender.send(listadoRutasABC)
    
def imprimirRutas(receiver: PipeConnection):
    listadoRutasABC = receiver.recv()
    print("---------------------------------------------------")
    for tuple in listadoRutasABC:
        print(f"{tuple[0]} - {tuple[1]}")
    print("---------------------------------------------------")

if __name__ == "__main__":
    left, right = Pipe()
    left1, right1 = Pipe()
    p1: Process = Process(target = crearRutas, args = (left,))
    p2: Process = Process(target = clasificarRutas, args = (right, left1))
    p3: Process = Process(target = imprimirRutas, args = (right1,))
    p1.start(); p2.start(); p3.start()
    p3.join()
    print("El hilo Main ha acabado de ejecutarse.")