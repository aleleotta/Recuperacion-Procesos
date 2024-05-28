from multiprocessing import Process, Pipe
from multiprocessing.connection import PipeConnection
from random import randint

def crearRutas(sender: PipeConnection):
    for i in range(10):
        ip: str = f"{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}"
        sender.send(ip)

def clasificarRutas(receiver: PipeConnection, sender: PipeConnection):
    for i in range(10):
        ip: str = receiver.recv()
        if int(ip.split(".")[0]) <= 223:
            sender.send(ip)
    sender.send(None)
    
def imprimirRutas(receiver: PipeConnection):
    ip = receiver.recv()
    while ip is not None:
        print("---------------------------------------------------")
        if int(ip.split(".")[0]) <= 127: #Class A
            print(ip, "Class A")
        elif int(ip.split(".")[0]) >= 128 and int(ip.split(".")[0]) <= 191: #Class B
            print(ip, "Class B")
        else: #Class C
            print(ip, "Class C")
        print("---------------------------------------------------")
        ip = receiver.recv()

if __name__ == "__main__":
    left, right = Pipe()
    left1, right1 = Pipe()
    p1: Process = Process(target = crearRutas, args = (left,))
    p2: Process = Process(target = clasificarRutas, args = (right, left1))
    p3: Process = Process(target = imprimirRutas, args = (right1,))
    p1.start(); p2.start(); p3.start()
    p3.join()
    print("El hilo Main ha acabado de ejecutarse.")