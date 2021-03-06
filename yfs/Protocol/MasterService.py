#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def newChunkServer(self, request):
    """
    When a new chunk server is going up, he will send the master,
    that he comes up and will send him information he have

    Parameters:
     - request
    """
    pass

  def getChunkLocations(self, fileIdentifier, length, offset):
    """
    Parameters:
     - fileIdentifier
     - length
     - offset
    """
    pass

  def getDefaultChunkSize(self):
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def newChunkServer(self, request):
    """
    When a new chunk server is going up, he will send the master,
    that he comes up and will send him information he have

    Parameters:
     - request
    """
    self.send_newChunkServer(request)
    self.recv_newChunkServer()

  def send_newChunkServer(self, request):
    self._oprot.writeMessageBegin('newChunkServer', TMessageType.CALL, self._seqid)
    args = newChunkServer_args()
    args.request = request
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_newChunkServer(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = newChunkServer_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    return

  def getChunkLocations(self, fileIdentifier, length, offset):
    """
    Parameters:
     - fileIdentifier
     - length
     - offset
    """
    self.send_getChunkLocations(fileIdentifier, length, offset)
    return self.recv_getChunkLocations()

  def send_getChunkLocations(self, fileIdentifier, length, offset):
    self._oprot.writeMessageBegin('getChunkLocations', TMessageType.CALL, self._seqid)
    args = getChunkLocations_args()
    args.fileIdentifier = fileIdentifier
    args.length = length
    args.offset = offset
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getChunkLocations(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getChunkLocations_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.fileNotFound is not None:
      raise result.fileNotFound
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getChunkLocations failed: unknown result");

  def getDefaultChunkSize(self):
    self.send_getDefaultChunkSize()
    return self.recv_getDefaultChunkSize()

  def send_getDefaultChunkSize(self):
    self._oprot.writeMessageBegin('getDefaultChunkSize', TMessageType.CALL, self._seqid)
    args = getDefaultChunkSize_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getDefaultChunkSize(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getDefaultChunkSize_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getDefaultChunkSize failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["newChunkServer"] = Processor.process_newChunkServer
    self._processMap["getChunkLocations"] = Processor.process_getChunkLocations
    self._processMap["getDefaultChunkSize"] = Processor.process_getDefaultChunkSize

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_newChunkServer(self, seqid, iprot, oprot):
    args = newChunkServer_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = newChunkServer_result()
    self._handler.newChunkServer(args.request)
    oprot.writeMessageBegin("newChunkServer", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getChunkLocations(self, seqid, iprot, oprot):
    args = getChunkLocations_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getChunkLocations_result()
    try:
      result.success = self._handler.getChunkLocations(args.fileIdentifier, args.length, args.offset)
    except FileNotFoundException, fileNotFound:
      result.fileNotFound = fileNotFound
    oprot.writeMessageBegin("getChunkLocations", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getDefaultChunkSize(self, seqid, iprot, oprot):
    args = getDefaultChunkSize_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getDefaultChunkSize_result()
    result.success = self._handler.getDefaultChunkSize()
    oprot.writeMessageBegin("getDefaultChunkSize", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class newChunkServer_args:
  """
  Attributes:
   - request
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'request', (NewChunkServerRequest, NewChunkServerRequest.thrift_spec), None, ), # 1
  )

  def __init__(self, request=None,):
    self.request = request

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.request = NewChunkServerRequest()
          self.request.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('newChunkServer_args')
    if self.request is not None:
      oprot.writeFieldBegin('request', TType.STRUCT, 1)
      self.request.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class newChunkServer_result:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('newChunkServer_result')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getChunkLocations_args:
  """
  Attributes:
   - fileIdentifier
   - length
   - offset
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'fileIdentifier', None, None, ), # 1
    (2, TType.I64, 'length', None, None, ), # 2
    (3, TType.I64, 'offset', None, None, ), # 3
  )

  def __init__(self, fileIdentifier=None, length=None, offset=None,):
    self.fileIdentifier = fileIdentifier
    self.length = length
    self.offset = offset

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.fileIdentifier = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.length = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.offset = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getChunkLocations_args')
    if self.fileIdentifier is not None:
      oprot.writeFieldBegin('fileIdentifier', TType.STRING, 1)
      oprot.writeString(self.fileIdentifier)
      oprot.writeFieldEnd()
    if self.length is not None:
      oprot.writeFieldBegin('length', TType.I64, 2)
      oprot.writeI64(self.length)
      oprot.writeFieldEnd()
    if self.offset is not None:
      oprot.writeFieldBegin('offset', TType.I64, 3)
      oprot.writeI64(self.offset)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getChunkLocations_result:
  """
  Attributes:
   - success
   - fileNotFound
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(ChunkLocation, ChunkLocation.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'fileNotFound', (FileNotFoundException, FileNotFoundException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, fileNotFound=None,):
    self.success = success
    self.fileNotFound = fileNotFound

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype28, _size25) = iprot.readListBegin()
          for _i29 in xrange(_size25):
            _elem30 = ChunkLocation()
            _elem30.read(iprot)
            self.success.append(_elem30)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.fileNotFound = FileNotFoundException()
          self.fileNotFound.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getChunkLocations_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter31 in self.success:
        iter31.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.fileNotFound is not None:
      oprot.writeFieldBegin('fileNotFound', TType.STRUCT, 1)
      self.fileNotFound.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getDefaultChunkSize_args:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getDefaultChunkSize_args')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getDefaultChunkSize_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I64, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I64:
          self.success = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getDefaultChunkSize_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I64, 0)
      oprot.writeI64(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
