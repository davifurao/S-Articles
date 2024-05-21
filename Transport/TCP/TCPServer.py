import socket

class TCPServer:    
    def __init__(self,host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def create_server(self, name='Servidor'):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen()
            print(name," escutando na porta", self.port)
        except Exception as e:
            print("Erro ao criar o servidor:", e)
            self.server_socket.close()
        
    def accept_connection(self):
        try:
            self.client_socket, addr = self.server_socket.accept()
            print("Conexão estabelecida com", addr)
        except Exception as e:
            print("Erro ao receber dados do cliente:", e)
        
    def receive_data(self,buffer_size=1024):
        try:
            data_received = self.client_socket.recv(buffer_size)
            #print("Dados recebidos do cliente:", data_received.decode())
            return data_received.decode()
        except Exception as e:
            print("Erro ao enviar dados ao cliente:", e)
    
    def sendMessagetoCLient(self, data):
        try:
            self.client_socket.sendall(data.encode())
            #print("Dados enviados ao cliente:", data)
        except Exception as e:
            print("Erro ao enviar dados ao cliente:", e)
        
    def close_connection(self):
        try:
            #self.client_socket.close()
            self.server_socket.close()
            print("Conexões fechadas.")
        except Exception as e:
            print("Erro ao fechar conexões:", e) 