import sys
from threading import Thread
import time

#calcula a sequência de Fibonacci (https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci)
# f(n) = f(n-1) + f(n-2)
# 0,1,1,2,3,5,8,13,21,34,55,89...
def fibo(n):
    if n>1:
        return fibo(n-1)+fibo(n-2)
    return n

#classe para simular um contador de tempo, que mostra uma mensagem 
#para o usuário enquanto o cálculo da sequência é realizado.
class Timer(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.encerar = False
        self.contando = False
        self.tempo = 0

    def finalizar(self):
        self.encerar = True
    
    def iniciar(self):
        self.contando = True
        self.start()
        

    def total(self):
        return self.tempo

    def run(self):
        while(not self.encerar):
            if(self.contando):
                if self.tempo % 2 == 0:
                    print("tic")
                else:
                    print("toc")
                self.tempo += 1
                time.sleep(1)
    


if __name__ == '__main__':
    
    n = int(sys.argv[1])

    timer = Timer()

    timer.iniciar()
    
    fibos = []
    for i in range(n):
        fibos.append(str(fibo(i)))


    timer.finalizar()
    
    print(','.join(fibos))
