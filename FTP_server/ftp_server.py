import socket


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (socket.gethostname(), 1001)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)

print('waiting for a connection')
connection, client_address = sock.accept()
print("connected to ", client_address)
print("")
while True:
    print("request a file from the connected computer ==> 1")
    print("send a file to the connected computer ==> 2")
    n=input("mode ==> ")
    connection.send(bytes(n, 'utf8'))

    n = int((connection.recv(1024)).decode("utf-8"))

    if(n==1):
        print("")
        print("input the filename that you request")
        filename=input("file name: ")
        connection.send(bytes(filename, 'utf8'))
        b=input("is it binary file (y/n):")
        connection.send(bytes(b, 'utf8'))

        if(b=="y"):
            len_data = int((connection.recv(1024)).decode("utf-8"))
            print(len_data)
            data=b""
            i=0
            while(True):
                data=data+connection.recv(65000)
                i+=1
                if(len_data<=len(data)):
                    break
            f=open(filename, "wb")
            f.write(data)
            f.close()
        else:
            len_data = int((connection.recv(1024)).decode("utf-8"))
            print(len_data)
            data=b""
            i=0
            while(True):
                data=data+connection.recv(65000)
                i+=1
                if(len_data<=len(data)):
                    break
            f=open(filename, "w")
            f.write(data.decode("utf-8"))
            f=open(filename, "w")
            f.close()

        print("recieved the file")
        print("data size: %d" % len(data))
        
    if(n==2):
        print("")
        print("choose a file to trasnfer..")
        filename=input("file name: ")        
        connection.send(bytes(filename, 'utf8'))
        
        b=input("is it binary file (y/n):")
        connection.send(bytes(b, 'utf8'))
        #got_file=connection.recv(1024)
        #print(got_file.decode("utf-8"))

        if(b=="y"):
            f=open(filename, "rb")
            data=f.read()
            connection.send(bytes(str(len(data)), "utf8"))
            i=0
            while(True):
                if(65000*i>=len(data)):
                    break
                try:
                    connection.send(data[65000*i:65000*(i+1)])
                except:
                    connection.send(data[65000*i:])
                    break
                print("%.2f percent" % (65000*i/len(data)*100))
                i+=1
            f.close()
        else:
            f=open(filename, "r")
            data=f.read()
            connection.send(bytes(str(len(data)), "utf8"))
            i=0
            while(True):
                if(65000*i>=len(data)):
                    break
                try:
                    connection.send(bytes(data[65000*i:65000*(i+1)], "utf8"))
                except:
                    connection.send(bytes(data[65000*i:], "utf8"))
                    break
                print("%.2f percent" % (65000*i/len(data)*100))
                i+=1
            f.close()
        
        print("sent the file..")

    break
connection.close()
