from multiprocessing import Process

def sumaArgumentos(num1, num2):
    suma = 0
    if num1 > num2:
        num1,num2 = num2,num1
    for i in range(num1, num2+1):
        suma = suma + i
    return suma

if __name__ == "__main__":
    pass