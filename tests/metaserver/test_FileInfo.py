from random import randint
from yfs.masterserver import DEFAULT_CHUNK_SIZE_BYTES
from yfs.masterserver.FileInfo import FileInfo


def test_exact_chunk_handles_conversion():
    # Arrange
    expected_chunk_handles_count = 10
    length = expected_chunk_handles_count * DEFAULT_CHUNK_SIZE_BYTES
    file_info = FileInfo("name", length)

    # Act
    chunk_handles_count = len(file_info.chunk_handles)

    # Assert
    assert expected_chunk_handles_count == chunk_handles_count


def get_length_by_handles_count(length):
    return (length * DEFAULT_CHUNK_SIZE_BYTES) + randint(1, 100)


def test_chunk_handles_conversion():
    # Arrange
    expected_chunk_handles_count = 8
    file_info = FileInfo("name", get_length_by_handles_count(expected_chunk_handles_count))

    # Act
    chunk_handles_count = len(file_info.chunk_handles)

    # Assert
    assert expected_chunk_handles_count == chunk_handles_count


def test_zero_offset_find_handles():
    # Arrange
    length = randint(3, 100)
    file_info = FileInfo("name1", get_length_by_handles_count(length))

    expected_handles_count = 2
    expected_chunk_handles = file_info.chunk_handles[:expected_handles_count]

    # Act
    handles = file_info.find_handles_for(expected_handles_count * DEFAULT_CHUNK_SIZE_BYTES)


    # Assert
    assert expected_handles_count == len(handles)
    assert expected_chunk_handles == handles


def test_given_offset_find_handles():
    # Arrange
    file_length = 24
    file_info = FileInfo("name1", get_length_by_handles_count(file_length))

    expected_handles_count = 3
    find_offset = 2
    expected_chunk_handles = file_info.chunk_handles[find_offset:find_offset + expected_handles_count]

    # Act
    handles = file_info.find_handles_for(expected_handles_count * DEFAULT_CHUNK_SIZE_BYTES, offset=find_offset * DEFAULT_CHUNK_SIZE_BYTES)


    # Assert
    assert expected_handles_count == len(handles)
    assert expected_chunk_handles == handles