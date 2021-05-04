from threading import Thread

from time import sleep
from random import randint


#classe que representa um objeto do tipo Thread. Note
# que esta classe extende a classe Thread do pacote threading.
#A sintaxe para extensão em python é class NOME_DA_CLASSE(SUPER_CLASSE):
class Trabalhador(Thread):

    def __init__(self,id):
        #o construtor da super-classe deve ser invocado, para que seja possível inicializar a thread
        Thread.__init__(self)
        self.mensagem = "Eu sou um trabalhador..."
        self.id=id

    def print_mensagem(self):
        print("{} {}".format(self.id,self.mensagem))
    

    #o método run serve para indicar o que a thread irá realizar. Enquanto o método run estiver rodando
    #a thread estará no ciclo de vida. Quando ele finalizar, a thread será morta. Geralmente dentro do método
    #run existe um laço de repetição
    def run(self):
        print("Iniciando thread...")
        x=0
        while(x<10):
            self.print_mensagem()
            sleep(randint(1,3))
            x+=1
        print("Finalizando thread.")


#Neste exemplo são criados 5 objetos da class Trabalhador. 
if __name__=='__main__':
    print("Processo iniciado...")
    trabalhadores = []
    for a in range(5):
        #aqui a thread é criada, porém ainda não está processando
        t = Trabalhador(a)
        #para que a thread seja de fato executada, é necessário invocar o método start
        t.start()
        trabalhadores.append(t)
    

    #indicamos que a thread principal deve aguardar os trabalhadores finalizarem suas tarefas
    for t in trabalhadores:
        t.join()
    print("Processo finalizado.")