import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Así podemos obtener el hostname de la máquina actual
host = socket.gethostname()
port = 9000

sock.bind((host, port))
sock.listen()

counter = 0
while counter < 5:
    try:
        socket_cliente, address = sock.accept()
        print("Conexión aceptada desde", address)
        socket_cliente.sendall("Gracias por conectarte\n".encode("ascii"))
        socket_cliente.close()
        counter += 1
    except ConnectionError:
        print("Ocurrió un error.")

sock.close()
