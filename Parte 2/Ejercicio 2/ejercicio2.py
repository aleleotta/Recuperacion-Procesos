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
        tuple[]
    

if __name__ == "__main__":
    left, right = Pipe()
    left1, right1 = Pipe()