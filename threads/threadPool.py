import concurrent.futures

from time import sleep
from random import randint


def tarefa(id):
    print(f"Iniciando thread...{id}")
    x=0
    while(x<2):
        sleep(randint(1,3))
        x+=1
    print(f"Finalizando thread...{id}")


if __name__=='__main__':
    print("Processo iniciado...")
    
    #define um gerenciador para executar as threads.
    #é possível informar o máximo de threads a serem executadas de forma concorrente
    #https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    
    for a in range(5):
        #submetemos a tarefa para ser executada.
        #Note que informamos o nome da função a ser executada, e sua lista de parâmetros
        executor.submit(tarefa,id=a)
    
    #chamamos o método shutdown para encerrar a submissão de tarefas para o gerenciador.
    #É possível informar que a thread principal ficará aguardando a finalização das tarefas
    #passando o parâmetro wait=True.
    executor.shutdown(wait=True)
    #executor.submit(tarefa,id=10)

    print("Processo finalizado.")
