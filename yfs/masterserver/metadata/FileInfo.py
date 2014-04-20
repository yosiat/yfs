import math
from yfs.masterserver import DEFAULT_CHUNK_SIZE_BYTES
from yfs.masterserver.metadata.Chunk import Chunk


class FileInfo(object):
    def __init__(self, name, length, chunks=None):
        """
        name - file name
        length - the length of the file in bytes
        chunks - set of chunk handles associated with this file
        """
        self.name = name
        self.length = length
        self.chunks = chunks or self._create_chunk_handles()

    def _create_chunk_handles(self):
        """
        Create chunk handles

        :return: list of Chunk
        """
        chunk_handles_count = self._calculate_chunks_count(self.length)
        handles = [Chunk() for _ in range(chunk_handles_count)]
        return handles

    def _calculate_chunks_count(self, length):
        """
        Calculate the chunks count using default chunk size and length
        :param length: length of blob/file in bytes
        :return: chunks count as integer
        """
        return int(math.ceil(length / DEFAULT_CHUNK_SIZE_BYTES))

    def find_chunks_for(self, length, offset=0):
        """
        Given a length and optional offset, the relevant handles will be returned

        :rtype : list of Chunk
        :param length: how to much to read in bytes
        :param offset: bytes count to skip
        """
        length_handles_count = self._calculate_chunks_count(length)

        offset_handles_count = self._calculate_chunks_count(offset)
        return self.chunks[offset_handles_count:offset_handles_count + length_handles_count]

    def get_chunk_by_handle(self, handle):
        for chunk in self.chunks:
            if chunk.handle == handle:
                return chunk

        return None