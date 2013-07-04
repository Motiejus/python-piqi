import sys
import json

from unittest import TestCase

from pypiqi import pypiqi

from pypiqi.tests.gen.person.piqi_pb2 import (person,
        phone_number, home, mobile, work)


class PersonTest(TestCase):
    def setUp(self):
        self.piqi = pypiqi.piqi()

    def tearDown(self):
        del self.piqi

    def test_encode_json(self):
        p = example_person()
        js = p.SerializeToJson(self.piqi)
        self.assertEqual(example_person_obj(), json.loads(js))

    def test_decode_json(self):
        js = json.dumps(example_person_obj())
        p1 = person()
        p1 = person.ParseFromJson(self.piqi, js)
        self.assertEqual(example_person_obj(), p1)


def example_person():
    p1 = person()
    p1.id = 0
    p1.name = "J. Random Hacker"
    p1.email = "j.r.hacker@example.com"
    n1, n2, n3 = p1.phone.add(), p1.phone.add(), p1.phone.add()
    n1.type = home; n1.number =  "(111) 123 45 67"
    n2.type = mobile; n2.number =  "(222) 123 45 67"
    n3.type = work; n3.number =  "(333) 123 45 67"
    return p1


def example_person_obj():
    return {
            "name": "J. Random Hacker",
            "id": 0,
            "email": "j.r.hacker@example.com",
            "phone": 
            [
                { "number": "(111) 123 45 67", "type": "home" },
                { "number": "(222) 123 45 67", "type": "mobile" },
                { "number": "(333) 123 45 67", "type": "work" }
                ]
            }

