from multiprocessing import Process, Pipe
from multiprocessing.connection import PipeConnection

def leerFicheroPeliculas(sender: PipeConnection, filePath: str, year: int):
    listadoPeliculasYear = []
    with open(filePath, "r") as doc:
        for line in doc:
            elementos = line.split(";")
            if int(elementos[1]) == year:
                listadoPeliculasYear.append(elementos[0])
    pack: tuple = (listadoPeliculasYear, year)
    sender.send(pack)

def escribirPeliculas(receiver: PipeConnection):
    pack = receiver.recv()
    with open(f"Parte 2/Ejercicio 4/PeliculasXXXX/Peliculas{pack[1]}.txt", "w") as doc:
        for pelicula in pack[0]:
            doc.write(pelicula + "\n")
            doc.flush()

if __name__ == "__main__":
    left, right = Pipe()
    filePath = "Parte 2/Ejercicio 4/peliculas.txt"
    year = int(input("Year: "))