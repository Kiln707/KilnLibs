from .serializationTag import SerializationTag
import sys, struct, select

class NetworkHandler:

    def __init__(self, socketFamily=socket.AF_INET, socketType=socket.SOCK_STREAM, socketProtocol=o, socketFileno=None):
        self.socket = socket.socket(family=socketFamily, type=socketType, proto=socketProtocol, fileno=socketFileno)

    def sendNetworkData(self, connection, tag):
        if isinstance(tag, Tag):
            connection.sendall(struct.pack('>i', len(data))+SerializationTag.encodePickle(tag))
        else:
            raise TypeError('Value tag, needs to be of Tag object.')

    def receiveNetworkData(self, connection):
        #data length is packed into 4 bytes
        total_len=0;total_data=bytearray();size=sys.maxsize
        sock_data=bytearray();recv_size=8192
        while total_len<size:
            sock_data=connection.recv(recv_size)
            if not sock_data:
                return None
            if not total_data:
                if len(sock_data)>4:
                    size=struct.unpack('>i', sock_data[:4])[0]
                    for b in sock_data[4:]:
                        total_data.append(b)
                elif len(sock_data) == 4:
                    size=struct.unpack('>i', sock_data[:4])[0]
            else:
                total_data.append(sock_data)
            total_len=len(total_data)
        return SerializationTag.decodePickle(bytes(total_data))

class NetworkClient(NetworkHandler):
    def __init__

class NetworkServer(NetworkHandler):
    def __init__(self,address, port, connections=5, socketFamily=socket.AF_INET, socketType=socket.SOCK_STREAM, socketProtocol=o, socketFileno=None):
        NetworkHandler.__init__(socketFamily, socketType,  socketProtocol, socketFileno)
        self.netsocket = initializeNetworkServer(address, port)

    def __del__(self):
        self.netsocket.close()

    def initializeNetworkServer(address, port, connections=5):
        print("Creating Network server listening on "+address+":"port)
        if address and port:
            try:
                self.netsocket.bind( address, port )
                self.netsocket.listen(connections)
                print("Network server creation complete.")
            except socket.error as msg:
                print("Failed to bind to"+address+":"+port,"Error Code:", str(msg[0]), 'Message:',msg[1])
        else:
            print('Failed to initialize network server. Bad address, port')
        self.netsocket = None
