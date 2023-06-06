#Instalar libreria requests
import requests 
from os import path
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target', help='Indicar el domnio de la victima')
parser= parser.parse_args()

def main():
    if parser.target:
        if path.exists('dataset_subdominios.txt'):
            wordlist=open('dataset_subdominios.txt','r')
            wordlist= wordlist.read().split('\n')
            for subdominio in wordlist:
                url="http://"+subdominio+"."+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("(+) Subdominio encontrado: " + url)

            for subdominio in wordlist:
                url="https://"+subdominio+"."+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("(+) Subdominio encontrado: " + url)

        else:
            print("(-) Ingrese un dominio")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()