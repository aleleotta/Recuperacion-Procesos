from multiprocessing import Process, Pool

def getVocals(vocal: str):
    count = 0
    file = open("Parte 2/Ejercicio 1/vocales.txt", "r")
    text = file.read()
    for character in text:
        if character == vocal:
            count = count + 1
    return count

if __name__ == "__main__":
    with Pool(processes = 5) as pool:
        vocales = ["a","e","i","o","u"]
        counts = pool.map(getVocals, vocales)
    print(
        f"a = {counts[0]}\ne = {counts[1]}\ni = {counts[2]}\no = {counts[3]}\nu = {counts[4]}\n"
    )