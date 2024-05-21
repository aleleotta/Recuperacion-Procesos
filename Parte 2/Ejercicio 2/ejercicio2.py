from multiprocessing import Process, Pipe
from multiprocessing.connection import PipeConnection
from random import randint

def crearRutas(sender: PipeConnection):
    listadoRutas = []
    for i in range(0, 11):
        ip: str = f"{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}"
        listadoRutas.append(ip)
    sender.send(listadoRutas)

def clasificarRutas(receiver: PipeConnection, sender: PipeConnection):
    listadoRutas = receiver.recv()
    listadoRutasABC = []
    

if __name__ == "__main__":
    left, right = Pipe()
    left1, right1 = Pipe()