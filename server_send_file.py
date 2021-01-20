import socket
from threading import Thread
from requests import get

TCP_IP = socket.gethostbyname(socket.gethostname())
print("The Server's IPv4 address is:", TCP_IP)

publicip = get("https://api.ipify.org").text
print("The Server's ext IP address is: " + publicip + " (Enter this if receiving files over the Internet)")

TCP_PORT = 8999

# Increase the buffer size if sending large files. Does not really affect smaller files.
BUFFER_SIZE = 1048576 # 1.048576 Mb took about 5min+ to transfer a 1Gb file

# filename = input("Enter the filename.type to send: ")

class ClientThread(Thread):

    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print("New thread started for "+ip+", "+str(port))

    def run(self):
        # f = open("./Files_to_send/" + filename, "rb")
        f = open(filename, "rb")
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                #print("Sent ",repr(l))
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print()
    filename = input("Enter the [filename.type] to send: ")
    print("Waiting for incoming connections...")
    print()
    (conn, (ip, port)) = tcpsock.accept()
    print("Connected to:", ip)
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)
