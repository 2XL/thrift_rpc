#!/usr/bin/env python


import sys, glob
sys.path.append('gen-py')

from tutorial import KVstore
from tutorial.ttypes import *

from shared.ttypes import SharedStruct

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class KVstoreHandler:
  def __init__(self):
    self.log = {}

	
  def put(Key, List):
    print 'put()'
	

  def get(Key):
    print 'get(key)'
    return None
	

  def add(Value, Key):
    print 'add()'
	

  def find(Value):
	print 'find()'
	return None

  def get_keys():
    print 'get_all()'
	return None

handler = KVstoreHandler()
processor = KVstore.Processor(handler)
transport = TSocket.TServerSocket(port=9091)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

# You could do one of these for a multithreaded server
#server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
#server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

print 'Starting the server...'
server.serve()
print 'done.'
