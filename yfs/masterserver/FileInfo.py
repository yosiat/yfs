from uuid import uuid4
import math
from yfs.masterserver import DEFAULT_CHUNK_SIZE_BYTES


class FileInfo(object):
    def __init__(self, name, length, chunk_handles=set()):
        """
        name - file name
        length - the length of the file in bytes
        chunk_handles - set of chunk handles associated with this file
        """
        self.name = name
        self.length = length
        self.chunk_handles = chunk_handles or self._create_chunk_handles()

    def _create_chunk_handles(self):
        chunk_handles_count = self._calculate_handles_count(self.length)
        handles = [uuid4() for _ in range(chunk_handles_count)]
        return handles

    def _calculate_handles_count(self, length):
        return int(math.ceil(length / DEFAULT_CHUNK_SIZE_BYTES))

    def find_handles_for(self, length, offset=0):
        """
        Given a length and optional offset, the relevant handles will be returned
        """
        length_handles_count = self._calculate_handles_count(length)
        offset_handles_count = self._calculate_handles_count(offset)
        return self.chunk_handles[offset_handles_count:offset_handles_count + length_handles_count]