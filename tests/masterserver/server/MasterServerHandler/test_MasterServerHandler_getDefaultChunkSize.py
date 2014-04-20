from yfs.masterserver.handler import MasterServerHandler
from yfs.masterserver import DEFAULT_CHUNK_SIZE_BYTES

def test_getDefaultChunkSize():
    master_server_handler = MasterServerHandler()
    assert DEFAULT_CHUNK_SIZE_BYTES == master_server_handler.getDefaultChunkSize()
