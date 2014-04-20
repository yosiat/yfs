from yfs.Protocol.ttypes import FileNotFoundException
from yfs.masterserver import DEFAULT_CHUNK_SIZE_BYTES
import logging


class MasterServerHandler:
    def __init__(self):
        self.file_name_to_file_info = dict()
        self.logger = logging.getLogger('MasterServerHandler')

    def up(self, ip, port):
        self.logger.info('MasterServer is serving requests')

    def newChunkServer(self, request):
        """
        When a new chunk server is going up, he will send the master,
        that he comes up and will send him information he have

        :rtype : object
        :param request:
        Parameters:
         - request
        """
        self.logger.info(
            "newChunkServer: {0}:{1} with files - {2}".format(request.chunkServerIP, request.chunkServerPort,
                                                              request.fileNameToChunkHandles.keys()))

        chunk_server_location = request.chunkServerIP, request.chunkServerPort

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
        chunks_locations = reduce(list.__add__, chunks_locations)

        self.logger.info(
            "getChunkLocations: file identifier: {0}, length: {1}, offset: {2} - return {3} chunk locations".format(
                fileIdentifier, length, offset, len(chunks_locations)))

        return chunks_locations


    def getDefaultChunkSize(self):
        """
        Returns the default chunk size
        :rtype : int
        :return: chunk size
        """
        self.logger.info("getDefaultChunkSize: {0}".format(DEFAULT_CHUNK_SIZE_BYTES))
        return DEFAULT_CHUNK_SIZE_BYTES





