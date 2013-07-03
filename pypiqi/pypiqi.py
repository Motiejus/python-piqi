
import json as json_mod
import subprocess
import struct

from gen.piqi_tools.piqi_pb2 import convert_input, json, pb, xml, piq
#from gen.piqi.piqi_pb2 import

class piqi(object):

    def __init__(self):
        self._server = subprocess.Popen(["piqi", "server"],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self._add_piqi = []

    def __del__(self):
        self._server.kill()

    def _add_to_piqi(self):
        """Send protobuf-encoded piqi specification to server"""
        pass

    def send_and_receive(self, packet):
        length = struct.pack(">I", len(packet))
        writable = length + packet
        print(''.join(["\\x%02X" % ord(x) for x in writable]))
        self._server.stdin.write(length + packet)
        self._server.stdin.flush()

        len_back = self._server.stdout.read(4)
        print(''.join(["\\x%02X" % ord(x) for x in len_back]))
        len2 = struct.unpack(">I", len_back)

        return self._server.stdout.read(len2)


    def generate(self, obj, output_fmt_str, json_omit_null_fields=True,
            pretty_print=True, use_strict_parsing=True):
        self._add_to_piqi(obj)
        inp = convert_input()

        if output_fmt_str == "json":
            output_fmt = json
        elif output_fmt_str == "pb":
            output_fmt = pb
        elif output_fmt_str == "xml":
            output_fmt = xml
        elif output_fmt_str == "piq":
            output_fmt = piq
        else:
            raise ValueError("bad output format: %s" % output_fmt_str)

        inp.data = obj.SerializeToString()
        inp.input_format = pb
        inp.json_omit_null_fields = json_omit_null_fields
        inp.output_format = output_format
        inp.pretty_print = pretty_print
        inp.type_name = obj.DESCRIPTOR.name
        inp.use_strict_parsing = use_strict_parsing

        stream = inp.SerializeToString()
        return self.send_and_receive(stream)
