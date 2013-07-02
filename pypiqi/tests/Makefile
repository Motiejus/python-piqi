
.INTERMEDIATE: person.piqi.proto

.PHONY: all clean test

all: person/piqi_pb2.py person/__init__.py

person/piqi_pb2.py: person.piqi.proto
	protoc --python_out=. $<

person/__init__.py: person/piqi_pb2.py
	touch person/__init__.py

person.piqi.proto: person.piqi
	piqi to-proto $<

clean: 
	rm -fr person *.pyc

test: all
	python -m unittest pypiqi_test
