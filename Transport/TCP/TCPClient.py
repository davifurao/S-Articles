import socket

class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print("Conexão estabelecida com o servidor.")
    
    def send_data(self, data):
        self.client_socket.sendall(data.encode())
        #print("Dados enviados ao servidor:", data)
    
    def receive_data(self):
        data_received = self.client_socket.recv(1024)
        #print("Resposta do servidor:", data_received.decode())
        return data_received.decode()
    
    def close(self):
        self.client_socket.close()
        print("Conexão encerrada.")
    
    def close_connection(self):
        try:
            self.client_socket.close()
            print("Conexões fechadas.")
        except Exception as e:
            print("Erro ao fechar conexões:", e)
