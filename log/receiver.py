# receiver.py
import socket

HOST = '0.0.0.0'  # Todas as interfaces
PORT = 12345  # A mesma porta que o contêiner de envio está enviando

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
                # Aqui você pode processar os dados recebidos conforme necessário
                with open("/app/text.txt","a") as f:
                    f.write(data.decode())
                    f.write('\n')
                print("Mensagem recebida:", data.decode())

if __name__ == "__main__":
    while True:
        main()
