
.PHONY: all clean test

.INTERMEDIATE: piqi_tools.piqi.proto

all: gen/piqi_tools/piqi_pb2.py gen/piqi_tools/__init__.py \
	gen/piqi/piqi_pb2.py gen/piqi/__init__.py

gen/piqi_tools/piqi_pb2.py: piqi_tools.piqi.proto
	protoc --python_out=gen $<

gen/piqi/piqi_pb2.py: piqi.piqi.proto
	protoc --python_out=gen $<

gen/piqi_tools/__init__.py: gen/piqi_tools/piqi_pb2.py
	touch $@

gen/piqi/__init__.py: gen/piqi/piqi_pb2.py
	touch $@

piqi_tools.piqi.proto: piqi_tools.piqi
	piqi to-proto $<

clean: 
	$(MAKE) $(MAKEARGS) -C tests clean
	rm -fr gen/piqi gen/piqi_tools *.pyc

test: all
	make -C tests test
