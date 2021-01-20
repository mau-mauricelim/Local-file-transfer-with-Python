import socket
import datetime

TCP_IP = input("Enter the Server's IP address: ")
TCP_PORT = 8999

BUFFER_SIZE = 1048576 # 1.048576 Mb/s

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

yymmdd = ''.join(str(datetime.datetime.now()).split()[0].split('-'))
hhmmss = ''.join(str(datetime.datetime.now()).split()[1].split(':')).split('.')[0]
yymmdd_hhmm = '_'.join([yymmdd, hhmmss])

desired_file_type = '.' + input("Enter the file.[type] you want to save as: ")
received_file = yymmdd_hhmm + desired_file_type

with open("./Received_files/"+received_file, 'wb') as f:
    print()
    print('File opened')
    while True:
        # print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        # print('data=%s', (data))
        if not data:
            f.close()
            # print('file close()')
            break
        # write data to a file
        f.write(data)

print('Successfully received the file')
# s.close()
print('Connection closed')
