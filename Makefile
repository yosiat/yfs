generate-thrift:
	thrift --gen py -out yfs/ thrift/Protocol.thrift
