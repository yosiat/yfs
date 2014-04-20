from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket, TTransport

from yfs import DEFAULT_MASTER_SERVER_PORT, DEFAULT_CHUNK_SERVER_PORT
from yfs.Protocol import ChunkService, MasterService
from yfs.chunkserver.handler import ChunkServerHandler
from yfs.masterserver.handler import MasterServerHandler
from yfs.utils.TCallbackSimpleServer import TCallbackSimpleServer


class ServerFactory(object):
    @staticmethod
    def create_chunk_server():
        handler = ChunkServerHandler()
        processor = ChunkService.Processor(handler)
        return ServerFactory.create_server(handler, processor, DEFAULT_CHUNK_SERVER_PORT)

    @staticmethod
    def create_master_server():
        handler = MasterServerHandler()
        processor = MasterService.Processor(handler)
        return ServerFactory.create_server(handler, processor, DEFAULT_MASTER_SERVER_PORT)


    @staticmethod
    def create_server(handler, processor, port):
        transport = TSocket.TServerSocket(port=port)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        simple_server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

        return TCallbackSimpleServer(simple_server, handler)