from random import randint
import yfs


def get_length_by_handles_count(length):
    return (length * yfs.masterserver.DEFAULT_CHUNK_SIZE_BYTES) + randint(1, 100)