import socket
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("socket created")
    ip_add="172.16.1.132"
    port = 3333
    complete_add = (ip_add,port)
    s.bind(complete_add)
    while True:
        message , sender_address = s.recvfrom(1024)

        print("Row message", message)
        print("Sender Address", sender_address)

        decoded_msg = message.decode("ascii")
        print("Message",decoded_msg)

except Exception as e:
    print("An error occured", e)