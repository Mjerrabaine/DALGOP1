from ast import For
import sys

def main():
    linea = sys.stdin.readline()
    casos = int(linea)
    linea = sys.stdin.readline()
    for i in range(0,casos):
        datastr =linea.split( )
        X = datastr[0] #string grande
        Y = datastr[1] #sub string
        m = datastr[2] #movimientos max?
        print("si esta leyendo")

main()