"""
    Tests:
        1. Should raise FileNotFound (test with populated)
        2. Should find the correct chunk handles
        3. Should specify the correct location
"""
from random import randint
from _pytest.python import raises
from yfs.Protocol.ttypes import FileNotFoundException
from yfs.masterserver.metadata.FileInfo import FileInfo
from yfs.masterserver.handler import MasterServerHandler
from tests.helper import get_length_by_handles_count

def test_raise_FileNotFound_getChunkLocations():
    # Arrange
    master_server_handler = MasterServerHandler()
    master_server_handler.file_name_to_file_info["kabuk"] = FileInfo("kabuk", get_length_by_handles_count(23))

    with raises(FileNotFoundException):
        master_server_handler.getChunkLocations("shnitzel", randint(0, 100), randint(0, 100))


def test_find_correct_chunks_and_locations_getChunkLocations():
    # Arrange
    master_server_handler = MasterServerHandler()
    file = FileInfo("name", get_length_by_handles_count(28))
    expected_location = ("ip1", "port1")
    expected_chunk_handle = file.chunks[2].handle

    file.chunks[2].locations = set([expected_location])
    master_server_handler.file_name_to_file_info[file.name] = file


    # Act
    chunk_locations = master_server_handler.getChunkLocations("name", get_length_by_handles_count(1), offset=get_length_by_handles_count(2))

    # Assert
    assert 1 == len(chunk_locations)

    first_chunk_location = chunk_locations[0]
    assert expected_chunk_handle == first_chunk_location.chunkHandle
    assert expected_location == (first_chunk_location.chunkServerIP, first_chunk_location.chunkServerPort)