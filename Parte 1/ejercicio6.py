from multiprocessing import Process, Pool

def sumaArgumentos(num1, num2):
    suma = 0
    if num1 > num2:
        num1,num2 = num2,num1
    for i in range(num1, num2+1):
        suma = suma + i
    return suma

if __name__ == "__main__":
    with Pool(processes = 3) as pool:
        numbers = [(0,10),(5,15),(45,85),(100, 50),(100, 200),(34,12),(56,2),(2,4),(5,4),(5,8)]
        results = pool.starmap(sumaArgumentos, numbers)
    print(results)