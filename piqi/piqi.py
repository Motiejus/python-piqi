
import json as json_mod
import subprocess
import struct

from gen.piqi_tools.piqi_pb2 import convert_input, add_piqi_input, \
        json, pb, xml, piq
from gen.piqi_rpc.piqi_pb2 import request as piqi_rpc_request, \
        response as piqi_rpc_response


class piqi(object):

    def __init__(self):
        self._server = subprocess.Popen(["piqi", "server"],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self._added_piqi = set()

    def __del__(self):
        self._server.kill()

    @staticmethod
    def _encode_rpc_request(name, bininput):
        req = request()
        req.name = name
        req.data = bininput
        return req

    def _add_piqi(self, obj):
        """Send protobuf-encoded piqi specification to server"""
        inp = add_piqi_input()
        inp.format = pb
        inp.data = obj._piqi_defn_pb
        self._rpc(inp.SerializeToString())

    def _rpc(self, request_name, payload):
        if self._pdict.get(obj.DESCRIPTOR.name) != "add_piqi":
            self._add_piqi(obj)
            self._pdict[obj.DESCRIPTOR.name] = "add_piqi"
        req = piqi_rpc_request()
        req.name = obj.DESCRIPTOR.name
        req.data = payload
        command = "\x00\x00\x00\x00" + req.SerializeToString()
        self._server.stdin.write(command)
        self._server.stdin.flush()
        len_back = self._server.stdout.read(4)
        len2 = struct.unpack(">I", len_back)
        resp = self._server.stdout.read(len2)
        ret = piqi_rpc_response()
        return ret.ParseFromString()



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
