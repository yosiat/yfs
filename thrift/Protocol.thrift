/**
 * ChunkReadRequest and ChunkReadResponse are callled 
 * at the very begining of the binary read chunk protocol.
 */
struct ChunkReadRequest {
  1: byte chunkHandle,
  2: i32 offset = 0
}

struct ChunkReadResponse {
  1: byte chunkHandle,
  2: i32 offset = 0,
  3: string checksum // TODO: Is string is the right type for checksum?
}

struct HeartbeatResposne {
  1: double totalDiskSpace,
  2: double usedDiskSpace,
  3: double freeDiskSpace,
  4: map<byte, i64> chunkHandleToReadCount
}

struct ChunkLocation {
  1: byte chunkHandle,
  2: string chunkServerIP,
  3: i32 chunkServerPort
}


struct NewChunkServerRequest {
  /**
   * File name to chunks, for example: 
   * - yosy.txt - 1,3,4
   */
  1: map<string, list<byte>> fileNameToChunkHandles 
}

service MasterService {
  /**
   * When a new chunk server is going up, he will send the master, 
   * that he comes up and will send him information he have
   */
  void newChunkServer(1: NewChunkServerRequest request),

  /*
   * When a client wants to read a file, he asks the master for the location of the chunks.
   * The parameters are:
   *  fileIdentifier
   *  length - how much the client wants to read in bytes
   *  offset - from where to start in bytes
   */
  list<ChunkLocation> getChunkLocations(1: string fileIdentifier, 2: i64 length, 3: i64 offset),

  /* 
   * Returns the default chunk size (64MB..)
   */
  i32 getDefaultChunkSize()
}


service ChunkService {
  /*
   * This heartbeat is issued once a while fromt the master to 
   * the chunk server.
   * We use this heartbeat request to get the metrics from the chunk size.
   */
  HeartbeatResposne heartbeat() 
}