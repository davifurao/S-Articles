from TCPServer import TCPServer

# Crie uma instância do TCPServer
server = TCPServer('127.0.0.1', 12345)

server.create_server()

server.accept_connection()

data_received = server.receive_data()
print("Dados recebidos do cliente:", data_received)
server.sendMessagetoCLient("Hello, client!")

server.close_connection()
