import socket
import datetime

HOST = '0.0.0.0'
PORT = 12345  # A mesma porta que o contêiner de envio está enviando
TOKEN = "lhama;" #token para autenticar usuário

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Conectado por', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
        
                #verificar se o token é valido e tirar ele do log
                arrdata = data.decode().split()
                
                
                with open("/app/log.txt","a+") as f:
                    if(arrdata[0] == TOKEN):
                        f.write(data.decode()[7:])
                        f.write('\n')
                    else:
                        data = datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
                        f.write(data)
                        f.write("; Serviço de Log; -1")
                        f.write('\n')

if __name__ == "__main__":
    while True:
        main()
