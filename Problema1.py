import sys
import time
from unittest import skip


def max_str( m, X ,Y ):
    counter=0  
    
    #cambio en letras para maximizar sub str
    for i in range (0,m):
        b=True
        c1=X.count(Y[0])
        c2=X.count(Y[1])
        if (c1<c2):
            j=0
            while b and j < len(X) :
                if X[j]!=Y[0]:
                    X[j]=Y[0]
                    b=False
                j+=1

        else:
            j= len(X)-1
            while b and j > 0:
                if X[j]!=Y[1]:
                    X[j]=Y[1]
                    b=False
                j-=1
        
       
           
            
           
       

               
           
    #contador
    for i in range(0, len(X)):
        
        if X[i]==Y[0]:
            interval=X[i+1:len(X)]
            counter+=interval.count(Y[1])
            
    return counter

#este metodo compara con el archivo de prueba que se nos dio
def porcentaje_correcto(comp):
    prueba = open('P1_cases.out','r')#pueden cambiar la direccion  que esta aqui para probar si quieren
    s=[]
    for i in range(0,len(comp)):
        temp=int(prueba.readline())
        s.append(temp)
    count=0
    for i in range(0,len(comp)):
        if (s[i]==comp[i]):
            count+=1
    return str(count*100 / len(comp))+"%"


def main():
    linea = sys.stdin.readline()
    casos = int(linea)
    linea = sys.stdin.readline()
    comp= []
    for i in range(0,casos):
        
        datastr =linea.split()
        x=list(datastr[0])
        y=list(datastr[1])
        m=int(datastr[2])
        result= max_str(m,x,y)
        comp.append(result)
        print(result)
        linea = sys.stdin.readline()
    #print(porcentaje_correcto(comp))#metodo de comparacion

start_time=time.time()
main()
print("--- %s tiempo segundos ---" % (time.time() - start_time))