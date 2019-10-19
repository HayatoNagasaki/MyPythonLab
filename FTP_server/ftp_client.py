



import socket
import subprocess, os

os.chdir("C:/Desktop")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('PC141224', 1001)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

connection=sock


while True:
    print("waiting for server")
    n=int((connection.recv(1024)).decode("utf-8"))
    connection.send(bytes(str(n), 'utf8'))

    if(n==1):
        filename = (connection.recv(1024)).decode("utf-8")
        b = (connection.recv(1024)).decode("utf-8")
        print(filename)
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

    
    if(n==2):
        filename=(connection.recv(1024)).decode("utf-8")
        b = (connection.recv(1024)).decode("utf-8")
        #sock.send(bytes("got filename "+filename, 'utf8'))

        
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
    break
    
    

sock.close()
