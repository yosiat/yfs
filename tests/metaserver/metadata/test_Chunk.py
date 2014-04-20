from uuid import UUID
from yfs.Protocol.ttypes import ChunkLocation
from yfs.masterserver.metadata.Chunk import Chunk


def test_generate_uuid_if_not_given_Chunk_init():
    # Arrange
    chunk = Chunk()

    # Act

    # Assert
    assert isinstance(chunk.handle, UUID)


def test_no_locations_create_chunk_locations():
    # Arrange
    chunk = Chunk()

    # Act
    locations = chunk.locations

    # Assert
    assert len(locations) == 0


def test_create_chunk_locations():
    # Arrange
    first_location = ("ip1", "port1")
    second_location = ("ip2", "port2")
    locations = list([first_location, second_location])
    chunk = Chunk(locations=locations)

    expected_locations = list()
    expected_locations.append(
        ChunkLocation(chunkHandle=chunk.handle, chunkServerIP=first_location[0], chunkServerPort=first_location[1])
    )
    expected_locations.append(
        ChunkLocation(chunkHandle=chunk.handle, chunkServerIP=second_location[0], chunkServerPort=second_location[1])
    )

    # Act
    chunk_locations = chunk.create_chunk_locations()

    # Assert
    assert expected_locations == chunk_locations
