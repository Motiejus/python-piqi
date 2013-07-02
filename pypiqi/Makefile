
.INTERMEDIATE: piqi_tools.piqi.proto

.PHONY: all clean test

all: piqi_tools/piqi_pb2.py

piqi_tools/piqi_pb2.py: piqi_tools.piqi.proto
	protoc --python_out=. $<

piqi_tools.piqi.proto: piqi_tools.piqi
	piqi to-proto $<

clean: 
	$(MAKE) $(MAKEARGS) -C tests clean
	rm -fr piqi_tools *.pyc

test: all
	make -C tests test
