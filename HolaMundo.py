import os 
import sys
#print(os.getcwd())
archivo = open("prueba.txt", "r", encoding="utf-8")
#print(archivo.read())

archivo = open("prueba.txt", "r")

for i in archivo:
    print(i.rstrip())
archivo.close()

archivo = open("datos.txt", "w")
archivo.write("Hola, este es un archivo python")
archivo.close()

archivo = open("datos.txt", "a")
archivo.writelines(["\nAhora", "\nEstamos", "\nAgregando", "\nMás", "\nLíneas"])
archivo.close()

sys.stderr.write("Error: No se pudo abrir el archivo.")
