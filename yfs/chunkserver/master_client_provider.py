from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport
from yfs import DEFAULT_MASTER_SERVER_PORT, DEFAULT_MASTER_SERVER_HOST
from yfs.Protocol import MasterService


"""
    MasterClientProivder - finds the current master, and returns a client
    connected to this master
"""


class MasterClientProvider:
    def __init__(self):
        pass

    def _find_connection_info(self):
        return DEFAULT_MASTER_SERVER_HOST, DEFAULT_MASTER_SERVER_PORT

    def create(self):
        host, port = self._find_connection_info()
        transport = TSocket.TSocket(host, port)

        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = MasterService.Client(protocol)
        transport.open()
        return client


    @staticmethod
    def get():
        provider = MasterClientProvider()
        return provider.create()