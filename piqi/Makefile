
.PHONY: all clean test

.INTERMEDIATE: gen/piqi_tools.piqi.proto

all: gen/piqi_tools/piqi_pb2.py gen/piqi_tools/__init__.py \
	gen/piqi/piqi_pb2.py gen/piqi/__init__.py \
	gen/piqi_rpc/piqi_pb2.py gen/piqi_rpc/__init__.py

gen/piqi_tools/piqi_pb2.py: gen/piqi_tools.piqi.proto
	protoc --python_out=. $<
gen/piqi_rpc/piqi_pb2.py: gen/piqi_rpc.piqi.proto
	protoc --python_out=. $<
gen/piqi/piqi_pb2.py: defn/piqi.piqi.proto
	protoc --python_out=gen $<
	mv gen/defn/piqi gen
	rmdir gen/defn


gen/piqi_tools/__init__.py: gen/piqi_tools/piqi_pb2.py
	touch $@
gen/piqi_rpc/__init__.py: gen/piqi_rpc/piqi_pb2.py
	touch $@
gen/piqi/__init__.py: gen/piqi/piqi_pb2.py
	touch $@

gen/piqi_tools.piqi.proto: defn/piqi_tools.piqi
	piqi to-proto $< -o $@
gen/piqi_rpc.piqi.proto: defn/piqi_rpc.piqi
	piqi to-proto $< -o $@

clean: 
	$(MAKE) $(MAKEARGS) -C tests clean
	rm -fr gen/piqi gen/piqi_tools gen/piqi_rpc *.pyc

test: all
	make -C tests test
