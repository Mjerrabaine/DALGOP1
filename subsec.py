from ast import For
import sys
from unittest import skip


def max_str( m, X ,Y ):
    counter=0  
    #cambio en letras para maximizar sub str
    for i in range (0,m):
        
        if ((i%2)==0):
            for j in reversed(range(0,len(X))):
                if X[j]!=Y[0]:
                    X[j]=Y[0]
                
               
               
        if ((i%2)==1):
            for j in range(0, len(X)):
                if X[j]!=Y[0]:
                    X[j]=Y[0]
               
           
          
    for i in range(0, len(X)):
        
        if X[i]==Y[0]:
            interval=X[i+1:len(X)]
            counter+=interval.count(Y[1])
            
    return X
    
def main():
    linea = sys.stdin.readline()
    casos = int(linea)
    linea = sys.stdin.readline()
    for i in range(0,casos):
        
        datastr =linea.split()
        x=list(datastr[0])
        y=list(datastr[1])
        m=int(datastr[2])
        result= max_str(m,x,y)
        print(result)
        linea = sys.stdin.readline()

main()