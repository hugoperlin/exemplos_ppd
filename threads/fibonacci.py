import sys

#calcula a sequência de Fibonacci (https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci)
# f(n) = f(n-1) + f(n-2)
# 0,1,1,2,3,5,8,13,21,34,55,89...

def fibo(n):
    if n>1:
        return fibo(n-1)+fibo(n-2)
    return n


if __name__ == '__main__':
    
    n = int(sys.argv[1])

    fibos = []
    for i in range(n):
        fibos.append(str(fibo(i)))

    print(','.join(fibos))
