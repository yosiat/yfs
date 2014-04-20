generate-thrift:
	rm -rf yfs/Protocol
	thrift --gen py -out yfs/ thrift/Protocol.thrift

test:
	py.test tests/
