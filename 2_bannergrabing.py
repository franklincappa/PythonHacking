import socket
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help='Indicar la ip de la victima:')
parser=parser.parse_args()

def banner(ip,port):
    s=socket.socket()
    s.connect((ip,port))
    print(str(s.recv(1024)))

def main():
    if parser.target:
        ip=parser.target
        port=21
        banner(ip,port)
    else:
        print("(-) Ingresa una IP")

if __name__ == '__main__':
    try: 
        main()
    except KeyboardInterrupt():
        sys.exit()
