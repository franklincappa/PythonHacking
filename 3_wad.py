#instalar libreria wad
import subprocess
import argparse
import sys

parser= argparse.ArgumentParser()
parser.add_argument('-t','--target', help='Indica la URL \n(e.h. https://ejemplo.com)')
parser= parser.parse_args()

def main():
    if parser.target:
        subprocess.call("wad -u " + parser.target + "> tecnologias.txt", shell=True)
        tecnologias = open("tecnologias.txt",'r')
        tecnologias =  tecnologias.read()
        tecnologias = tecnologias.split("[")
        tecnologias = tecnologias[1].split("]")
        tecnologias = tecnologias[0].split("{")
        
        file=open('tecnologias.txt','w')
        for tecnologia in tecnologias:
            nuevo = tecnologia.replace('\n','')
            nuevo = nuevo.replace('      ','')
            nuevo = nuevo.replace('"','')
            nuevo = nuevo.replace('}','')
            nuevo =  nuevo[0]
            nuevo = nuevo.replace(',','\n')

            print(nuevo)
            print("*"*20)
    else:
        print("(-) Ingrese una URL ")

if __name__== '__main__':
    try: 
        main()
    except KeyboardInterrupt:
        sys.exit()