#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import shared.SharedService
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface(shared.SharedService.Iface):
  def publish(self, topic, msg):
    """
    Parameters:
     - topic
     - msg
    """
    pass


class Client(shared.SharedService.Client, Iface):
  def __init__(self, iprot, oprot=None):
    shared.SharedService.Client.__init__(self, iprot, oprot)

  def publish(self, topic, msg):
    """
    Parameters:
     - topic
     - msg
    """
    self.send_publish(topic, msg)
    self.recv_publish()

  def send_publish(self, topic, msg):
    self._oprot.writeMessageBegin('publish', TMessageType.CALL, self._seqid)
    args = publish_args()
    args.topic = topic
    args.msg = msg
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_publish(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = publish_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    return


class Processor(shared.SharedService.Processor, Iface, TProcessor):
  def __init__(self, handler):
    shared.SharedService.Processor.__init__(self, handler)
    self._processMap["publish"] = Processor.process_publish

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

  def process_publish(self, seqid, iprot, oprot):
    args = publish_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = publish_result()
    self._handler.publish(args.topic, args.msg)
    oprot.writeMessageBegin("publish", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class publish_args(object):
  """
  Attributes:
   - topic
   - msg
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'topic', None, None, ), # 1
    (2, TType.STRUCT, 'msg', (Message, Message.thrift_spec), None, ), # 2
  )

  def __init__(self, topic=None, msg=None,):
    self.topic = topic
    self.msg = msg

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
          self.topic = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.msg = Message()
          self.msg.read(iprot)
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
    oprot.writeStructBegin('publish_args')
    if self.topic is not None:
      oprot.writeFieldBegin('topic', TType.STRING, 1)
      oprot.writeString(self.topic)
      oprot.writeFieldEnd()
    if self.msg is not None:
      oprot.writeFieldBegin('msg', TType.STRUCT, 2)
      self.msg.write(oprot)
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

class publish_result(object):

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
    oprot.writeStructBegin('publish_result')
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
