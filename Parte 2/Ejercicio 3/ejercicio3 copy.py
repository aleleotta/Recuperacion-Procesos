from multiprocessing import Process, Queue
from random import uniform

def generarNumeros(queue: Queue, filePath: str):
    with open(filePath, "w") as doc:
        for i in range(6):
            num: float = round(uniform(0, 10.000001), 2)
            doc.write(str(num) + " \n")
    queue.put(filePath)

def calcularMedias(queue: Queue, nombreAlumno: str):
    filePathNotas = queue.get()
    listadoNotas: list = []
    with open(filePathNotas, "r") as doc:
        for line in doc:
            listadoNotas.append(line)
    filePathMedias: str = "Parte 2/Ejercicio 3/medias.txt"
    with open(filePathMedias, "a") as doc:
        average: float = 0
        count: int = 0
        for nota in listadoNotas:
            average = average + float(nota)
            count = count + 1
        average = average / count
        doc.write(f"{nombreAlumno} {average}\n")
        doc.flush()
    queue.put(filePathMedias)

def imprimirNotaMaxima(queue: Queue):
    filePathMedias = queue.get()
    with open(filePathMedias, "r") as doc:
        notaMaxima: float = 0
        nombreAlumno: str = ""
        for line in doc:
            if line != "":
                valores = line.split()
                if notaMaxima < float(valores[1]):
                    nombreAlumno = valores[0]
                    notaMaxima = float(valores[1])
    print("------------------------------------------------")
    print(f"Alumno: {nombreAlumno}\n")
    print(f"Nota maxima: {notaMaxima}")
    print("------------------------------------------------")


if __name__ == "__main__":
    queue = Queue()
    nombres = ["Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "James", "Isabella", "Benjamin"]
    listadoProcesos = []
    with open("Parte 2/Ejercicio 3/medias.txt", "w") as doc:
        doc.write("")
        doc.flush()
    for i in range(10):
        filePath = f"Parte 2/Ejercicio 3/Notas/notas{i}.txt"
        p1: Process = Process(target = generarNumeros, args = (queue, filePath))
        p1.start()
        listadoProcesos.append(p1)
    for p in listadoProcesos:
        p.join()
    for i in range(10):
        pass
    print("\nTodos los procesos han terminado.\n")