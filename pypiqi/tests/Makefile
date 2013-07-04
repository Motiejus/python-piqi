
.PHONY: all clean test

all: gen/person/piqi_pb2.py gen/person/__init__.py gen/person.piqi.pb

gen/person/piqi_pb2.py: gen/person.piqi.proto $(GEN)
	protoc --python_out=. $<

gen/person/__init__.py: gen/person/piqi_pb2.py
	touch $@

gen/person.piqi.proto: person.piqi gen/person.piqi.pb
	piqi to-proto $< -o $@

gen/person.piqi.pb: person.piqi
	piqi convert person.piqi -f piqi -t pb -o gen/person.piqi.pb

clean: 
	rm -fr gen/person gen/person.piqi.pb gen/person.piqi.proto *.pyc

test: all
	python -m unittest pypiqi_test
