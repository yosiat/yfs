import logging
from yfs.Protocol.ttypes import NewChunkServerRequest
from yfs.chunkserver.master_client_provider import MasterClientProvider


class ChunkServerHandler:
    def __init__(self):
        self.master = MasterClientProvider.get()
        self.logger = logging.getLogger('ChunkServerHandler')



    def up(self, ip, port):
        self.logger.info('ChunkServer is serving requests')
        self.logger.info('Sending NewChunkServerRequest to the master')

        request = NewChunkServerRequest()
        request.chunkServerIP = ip
        request.chunkServerPort = port

        request.fileNameToChunkHandles = dict()
        self.master.newChunkServer(request)

    def heartbeat(self):
        pass
