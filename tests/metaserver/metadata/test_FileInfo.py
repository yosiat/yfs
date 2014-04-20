from random import randint
import uuid
import yfs.masterserver
from yfs.masterserver.metadata.Chunk import Chunk
from yfs.masterserver.metadata.FileInfo import FileInfo


def test_exact_chunk_handles_conversion():
    # Arrange
    expected_chunk_handles_count = 10
    length = expected_chunk_handles_count * yfs.masterserver.DEFAULT_CHUNK_SIZE_BYTES
    file_info = FileInfo("name", length)

    # Act
    chunk_handles_count = len(file_info.chunks)

    # Assert
    assert expected_chunk_handles_count == chunk_handles_count


def get_length_by_handles_count(length):
    return (length * yfs.masterserver.DEFAULT_CHUNK_SIZE_BYTES) + randint(1, 100)


def test_chunk_handles_conversion():
    # Arrange
    expected_chunk_handles_count = 8
    file_info = FileInfo("name", get_length_by_handles_count(expected_chunk_handles_count))

    # Act
    chunk_handles_count = len(file_info.chunks)

    # Assert
    assert expected_chunk_handles_count == chunk_handles_count


def test_zero_offset_find_handles():
    # Arrange
    length = randint(3, 100)
    file_info = FileInfo("name", get_length_by_handles_count(length))

    expected_handles_count = 2
    expected_chunk_handles = file_info.chunks[:expected_handles_count]

    # Act
    handles = file_info.find_chunks_for(expected_handles_count * yfs.masterserver.DEFAULT_CHUNK_SIZE_BYTES)


    # Assert
    assert expected_handles_count == len(handles)
    assert expected_chunk_handles == handles


def test_given_offset_find_handles():
    # Arrange
    file_length = 24
    file_info = FileInfo("name", get_length_by_handles_count(file_length))

    expected_handles_count = 3
    find_offset = 2
    expected_chunk_handles = file_info.chunks[find_offset:find_offset + expected_handles_count]

    # Act
    handles = file_info.find_chunks_for(expected_handles_count * yfs.masterserver.DEFAULT_CHUNK_SIZE_BYTES,
                                        offset=find_offset * yfs.masterserver.DEFAULT_CHUNK_SIZE_BYTES)

    # Assert
    assert expected_handles_count == len(handles)
    assert expected_chunk_handles == handles

def test_find_handles():
    # Arrange
    CHUNK_LENGTH = 2
    chunks = [Chunk() for _ in range(CHUNK_LENGTH)]
    file_info = FileInfo("name", get_length_by_handles_count(CHUNK_LENGTH), chunks)

    expected_chunk = chunks[1]

    # Act
    chunk = file_info.get_chunk_by_handle(expected_chunk.handle)

    # Assert
    assert expected_chunk == chunk

def test_not_exist_chunk_find_handle():
    # Arrange
    file_info = FileInfo("name", get_length_by_handles_count(8))
    expected_chunk = None

    # Act
    found_chunk = file_info.get_chunk_by_handle(uuid.uuid4())

    # Assert
    assert  expected_chunk == found_chunk






















