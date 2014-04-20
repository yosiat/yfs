from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from yfs.Protocol.MasterService import Processor
from yfs.Protocol.ttypes import FileNotFoundException
from yfs.masterserver import DEFAULT_CHUNK_SIZE_BYTES


class MasterServerHandler:
    def __init__(self):
        self.file_name_to_file_info = dict()

    def newChunkServer(self, request):
        """
        When a new chunk server is going up, he will send the master,
        that he comes up and will send him information he have

        :rtype : object
        :param request:
        Parameters:
         - request
        """
        chunk_server_location = request.chunkServerIP, request.chunkServerPort

        # Make sure that map<?,?> is dict
        for file_name, chunk_handles in request.fileNameToChunkHandles.viewitems():
            file_info = self.file_name_to_file_info.get(file_name)
            if file_info is None:
                # We should probably, throw error? or create this file?
                continue

            chunks = [file_info.get_chunk_by_handle(handle) for handle in chunk_handles]

            for chunk in chunks:
                chunk.locations.update([chunk_server_location])

    def getChunkLocations(self, fileIdentifier, length, offset):
        """
        Parameters:
         - fileIdentifier
         - length
         - offset
        """
        file_info = self.file_name_to_file_info.get(fileIdentifier, None)
        if file_info is None:
            raise FileNotFoundException(fileIdentifier=fileIdentifier)

        chunks = file_info.find_chunks_for(length, offset)
        chunks_locations = [chunk.create_chunk_locations() for chunk in chunks]

        return reduce(list.__add__, chunks_locations)


    def getDefaultChunkSize(self):
        """
        Returns the default chunk size
        :rtype : int
        :return: chunk size
        """
        return DEFAULT_CHUNK_SIZE_BYTES



class MasterServerFactory(object):
    @staticmethod
    def getServer():
        handler = MasterServerHandler()
        processor = Processor(handler)
        transport = TSocket.TServerSocket(port=9090)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()

        return TServer.TSimpleServer(processor, transport, tfactory, pfactory)

