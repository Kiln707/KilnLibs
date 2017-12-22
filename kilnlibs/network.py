from .serializationTag import SerializationTag
import sys, struct, select

class NetworkHandler:

    def __init__(self, socketFamily=socket.AF_INET, socketType=socket.SOCK_STREAM, socketProtocol=o, socketFileno=None):
        self.socket = socket.socket(family=socketFamily, type=socketType, proto=socketProtocol, fileno=socketFileno)

    def __del__(self):
        self.socket.close()

    def sendData(self, connection, tag):
        if isinstance(tag, Tag):
            self.socket.sendall(struct.pack('>i', len(data))+SerializationTag.encodePickle(tag))
        else:
            raise TypeError('Value tag, needs to be of Tag object.')

    def receiveData(self, connection):
        #data length is packed into 4 bytes
        total_len=0;total_data=bytearray();size=sys.maxsize
        sock_data=bytearray();recv_size=8192
        while total_len<size:
            sock_data=self.socket.recv(recv_size)
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
    def __init__(self, address='127.0.0.1', port='65432', socketFamily=socket.AF_INET, socketType=socket.SOCK_STREAM, socketProtocol=o, socketFileno=None):
        NetworkHandler.__init__(socketFamily, socketType, socketProtocol, socketFileno)
        self.connect(address, port)

    def connect(address, port):
        self.socket = self.socket.connect( (address, port) )


class NetworkServer(NetworkHandler):
    def __init__(self,address, port, connections=5, socketFamily=socket.AF_INET, socketType=socket.SOCK_STREAM, socketProtocol=o, socketFileno=None):
        NetworkHandler.__init__(socketFamily, socketType,  socketProtocol, socketFileno)
        self.initializeNetworkServer(address, port)
        self.connections = {}
        self.readlist = []
        self.writelist = []
        self.errorlist = []

    def initializeNetworkServer(address, port, connections=5):
        print("Creating Network server listening on "+address+":"port)
        if address and port:
            try:
                self.socket.bind( address, port )
                self.socket.listen(connections)
                print("Network server creation complete.")
            except socket.error as msg:
                print("Failed to bind to"+address+":"+port,"Error Code:", str(msg[0]), 'Message:',msg[1])
                self.socket=None
        else:
            print('Failed to initialize network server. Bad address, port')
            self.socket = None

    def acceptIncomingConnections():
        readable, writable, errored = select.select([self.socket], [],[], 0.5)
        for s in readable:
            connection, address = self.socket.accept()
            self.readlist.append(connection)
            self.connections[connection] = address

    def receiveData():
        returndata = []
        readable, writable, errored = select.select(self.readlist, [],[], 0.5)
        for s in readable:
            returndata.append( (s, self.receiveData(s)) )
        return returndata
