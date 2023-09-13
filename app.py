
import time
import threading

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CRITERIO DE ARRANQUE: SE REGULA SEGÚN A CLIENTE
def timer(timer_runs):  
    while timer_runs.is_set():  
              try:                      
                    print("Hola Mundo")
              except Exception as error: 
                    print("Error")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
              time.sleep(10)   #ACA SE REGULA EL TIEMPO DE EJECUCION DEL BOT     
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
#Arrancamos el Sustema Cada Minuntos Despues de Realizar Cada Caso  
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,)) 
t.start()      
        
