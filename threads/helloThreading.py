#o pacote threading permite criar threas em python
import threading
from threading import Thread

import time

#esta é a função de trabalho que será executada pelas threads. É possível passar
#parâmetros para a função.
def funcao(i):
    #a partir do pacote threading é possível saber qual é a thread que está sendo executada no momento
    #através do método threading.currentThread().
    print(f"{threading.currentThread().getName()} - Imprimindo {i}")
    time.sleep(2)


#
if __name__=="__main__":

    #pegando o nome da thread atual, que neste caso será a MainThread
    nome = threading.currentThread().getName()

    print(f"{nome} - Iniciando...")

    #serão criadas 5 threads. Para indicar qual é a função de trabalho
    #passamos pelo parâmetro target o nome da função. Note que não utilizamos
    #parênteses, isso porque estamos passando um "ponteiro" para a função.
    #Também é possível indicar uma tupla com os parâmetros para a função a ser executada.
    threads=[]
    for a in range(5):
        #criando uma thread, indicando a função a ser executada e seus parâmetros.
        #Neste momento a thread somente está criada, porém ainda não está executando
        #a função.
        t = Thread(target=funcao,args=(a,))
        #a thread começa a executar a função quando o método start é invocado.
        t.start()
        threads.append(t)
    
    #caso seja necessário, é possível indicar para a thread principal
    #aguardar que as threas secundárias finalizem o trabalho. Isso é feito
    #invocando o método join em cada uma das threads secundárias.
    for t in threads:
        t.join()

    print(f"{nome} - Finalizando...")



