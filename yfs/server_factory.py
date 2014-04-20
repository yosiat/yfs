from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket, TTransport
from yfs.Protocol.MasterService import Processor
from yfs.masterserver.server import MasterServerHandler



class ServerFactory(object):

    @staticmethod
    def create_master_server():
        handler = MasterServerHandler()
        processor = Processor(handler)
        return ServerFactory.create_server(processor)

    

    @staticmethod
    def create_server(processor):
        transport = TSocket.TServerSocket(port=9090)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()

        return TServer.TSimpleServer(processor, transport, tfactory, pfactory)