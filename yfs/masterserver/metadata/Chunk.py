from uuid import uuid4
from yfs.Protocol.ttypes import ChunkLocation


class Chunk(object):
    def __init__(self, handle=None, checksum=None, locations=None):
        """
        Chunk

        :param handle: UUID
        :param checksum: string of checksum
        :param locations: list of tuples (host, port)
        """
        self.handle = handle or uuid4()
        self.checksum = checksum
        self.locations = locations or set()

    def create_chunk_locations(self):
        return [
            ChunkLocation(chunkHandle=self.handle, chunkServerIP=ip, chunkServerPort=port)
            for ip, port in self.locations
        ]

