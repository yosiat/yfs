/**
 * ChunkReadRequest and ChunkReadResponse are callled 
 * at the very begining of the binary read chunk protocol.
 */
struct ChunkReadRequest {
  1: i64 chunkHandle,
  2: i32 offset = 0
}

struct ChunkReadResponse {
  1: i64 chunkHandle,
  2: i32 offset = 0,
  3: string checksum // TODO: Is string is the right type for checksum?
}

struct HeartbeatResposne {
  1: double totalDiskSpace,
  2: double usedDiskSpace,
  3: double freeDiskSpace 
  3: map<i64, i64> chunkHandleToReadCount
}


struct NewChunkServerRequest {
  /**
   * File name to chunks, for example: 
   * - yosy.txt - 1,3,4
   */
  1: map<string, list<i64>> fileNameToChunkHandles 
}

service MasterService {
  /**
   * When a new chunk server is going up, he will send the master, 
   * that he comes up and will send him information he have
   */
  void newChunkServer(1: NewChunkServerRequest request),

  /*
   * When a client wants to read a file, he asks the master for the location of the chunks
   * The client should have: the file identifier, and offset.
   * Because the client know the default chunk size, he can calculate the index.
   */
  list<ChunkLocation> getChunkLocations(1: string fileIdentifier, 2: i64 chunkIndex),

  /* 
   * Returns the default chunk size (64MB..)
   */
  i64 getDefaultChunkSize()
}


service ChunkService {
  /*
   * This heartbeat is issued once a while fromt the master to 
   * the chunk server.
   * We use this heartbeat request to get the metrics from the chunk size.
   */
  HeartbeatResposne heartbeat() 
}



































