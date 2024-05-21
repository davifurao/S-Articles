from TCPClient import TCPClient

client = TCPClient('127.0.0.1', 12345)
client.connect()


client.send_data("Hello, server!")
response = client.receive_data()
print("Resposta do servidor:", response)

client.close_connection()
