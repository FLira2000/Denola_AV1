from HeapSort import *

def main():
    arr = []
    n = 0
    while True:
        n = input("Entre com números para o array('q' para finalizar): ")
        if n == 'q':
            break
        
        arr.append(n)
    heapSort(arr)
    print(arr)

main()
