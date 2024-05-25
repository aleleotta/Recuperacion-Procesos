from multiprocessing import Process

def sumaArgumentos(num1, num2):
    suma = 0
    if num1 > num2:
        num1,num2 = num2,num1
    for i in range(num1, num2+1):
        suma = suma + i
    print(suma)

if __name__ == "__main__":
    numbers = [0, 10, 5, 15, 45, 85, 100, 50, 100, 200, 34, 12, 56, 2, 2, 4, 5, 4, 5, 8]
    for i in range(0,19,2):
        p = Process(target = sumaArgumentos, args = (numbers[i], numbers[i+1]))
        p.start()
        """if i == 18:
            p.join()"""
    p.join()
    print("All processes have been terminated.")