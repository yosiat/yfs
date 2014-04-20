
from random import randint
from tests.helper import get_length_by_handles_count
from yfs.Protocol.ttypes import NewChunkServerRequest
from yfs.masterserver.metadata.Chunk import Chunk
from yfs.masterserver.metadata.FileInfo import FileInfo
from yfs.masterserver.server import MasterServerHandler


def create_file(name, handles_count):
    return FileInfo(name, get_length_by_handles_count(handles_count))


def test_file_dosent_exist_newChunkServer():
    # Arrange
    master_server_handler = MasterServerHandler()

    chunk_handle = Chunk().handle
    file_name = randint(1, 100)

    # - create the request
    fake_request = NewChunkServerRequest(fileNameToChunkHandles=dict())
    fake_request.fileNameToChunkHandles[file_name] = [chunk_handle]

    # Act
    master_server_handler.newChunkServer(fake_request)

    # Assert
    assert file_name not in master_server_handler.file_name_to_file_info


def test_add_location_to_matching_chunk_and_file_newChunkServer():
    # Arrange
    master_server_handler = MasterServerHandler()


    # - create two files
    first_file = create_file("first", 3)
    second_file = create_file("second", 5)

    # - populate each files with locations
    dummy_first_location = ("ip1", "port1")
    dummy_second_location = ("ip2", "port2")

    first_file_chunk_handle = first_file.chunks[2].handle
    second_file_chunk_handle = second_file.chunks[4].handle

    first_file.chunks[2].locations.update([dummy_first_location])
    second_file.chunks[4].locations.update([dummy_second_location])


    # - add the files
    master_server_handler.file_name_to_file_info[first_file.name] = first_file
    master_server_handler.file_name_to_file_info[second_file.name] = second_file

    # - create the request
    fake_request = NewChunkServerRequest(fileNameToChunkHandles=dict())
    fake_request.chunkServerIP, fake_request.chunkServerPort = dummy_first_location
    fake_request.fileNameToChunkHandles[first_file.name] = [first_file_chunk_handle]
    fake_request.fileNameToChunkHandles[second_file.name] = [second_file_chunk_handle]

    # Act
    master_server_handler.newChunkServer(fake_request)
    first_first_after = master_server_handler.file_name_to_file_info[first_file.name]
    second_first_after = master_server_handler.file_name_to_file_info[second_file.name]

    first_chunk_locations = first_first_after.get_chunk_by_handle(first_file_chunk_handle).locations
    second_chunk_locations = second_first_after.get_chunk_by_handle(second_file_chunk_handle).locations

    # Assert
    assert set([dummy_first_location]) == first_chunk_locations
    assert set([dummy_first_location, dummy_second_location]) == second_chunk_locations

def test_dont_add_location_twice_newChunkServer():
    # Arrange
    master_server_handler = MasterServerHandler()

    # - create two files
    first_file = create_file("first", 3)

    # - populate each files with locations
    dummy_first_location = ("ip1", "port1")
    first_file_chunk_handle = first_file.chunks[2].handle

    first_file.chunks[2].locations.update([dummy_first_location])

    # - add the files
    master_server_handler.file_name_to_file_info[first_file.name] = first_file

    # - create the request
    fake_request = NewChunkServerRequest(fileNameToChunkHandles=dict())
    fake_request.chunkServerIP, fake_request.chunkServerPort = dummy_first_location
    fake_request.fileNameToChunkHandles[first_file.name] = [first_file_chunk_handle]

    # Act
    master_server_handler.newChunkServer(fake_request)
    first_first_after = master_server_handler.file_name_to_file_info[first_file.name]
    first_chunk_locations = first_first_after.get_chunk_by_handle(first_file_chunk_handle).locations

    # Assert
    assert set([dummy_first_location]) == first_chunk_locations
    assert 1 == len(first_chunk_locations)