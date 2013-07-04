Python wrapper to piqi
----------------------

This project is a proof-of-concept python and piqi bridge.

What is piqi?
-------------

Piqi is a tool which lets you define a datatype (or interface), and use it using
google protocol buffers, json, xml and piq.

Quick example
-------------

For example, let's make an `equivalent person`_ definition::

    .record [
        .name person
        .field [ .name name .type string ]
        .field [ .name id .type int ]
        .field [ .name email .type string .optional ]
        .field [ .name phone .type phone-number .repeated ]
    ]

    .record [
        .name phone-number
        .field [ .name number .type string ]
        .field [ .name type .type phone-type .optional .default.home ]
    ]

    .enum [
        .name phone-type
        .option [ .name mobile ]
        .option [ .name home ]
        .option [ .name work ]
    ]

API is nearly equivalent to gpb api::

    >>> p1 = person()
    >>> p1.id = 0
    >>> p1.name = "J. Random Hacker"
    >>> p1.email = "j.r.hacker@example.com"
    >>> n1 = p1.phone.add()
    >>> n1.type = home; n1.number =  "(111) 123 45 67"
    >>> p1.SerializeToJson()
    '{
        "name": "J. Random Hacker",
        "id": 0,
        "email": "j.r.hacker@example.com",
        "phone": [{"number":"(111) 123 45 67","type":"work"}]
    }'
    >>> p1.SerializeToXML()
    '<?xml version="1.0" encoding="UTF-8"?>
    <value>
        <name>J. Random Hacker</name>
        <id>0</id>
        <email>j.r.hacker@example.com</email>
        <phone>
            <number>(111) 123 45 67</number>
            <type>work</type>
        </phone>
    </value>'
    >>> p1.SerializeToString()
    # serialize to gpb. Terminal hangs.

In short, **you can define your service type, and use ping it in json, xml or
pb**.  For data definition google protocol buffers is a great idea, but is way
better to do JSON from browser. So you are free to use whatever transport you
want with a Schema to rule them.

Wrapper information
-------------------

Python application works as follows: it opens piqi binary (``piqi server``) and
simply talks undocumented, gpb-based binary protocol. See `reference
implementation`_ in Erlang.

I started wrapper implementation during EuroPython 2013, but could not finish
it. It is unlikely that I will finish it soon (because I am using piqi from
Erlang), unless you ping me on `piqi mailing list`_.

.. _`equivalent person`: https://developers.google.com/protocol-buffers/docs/overview
.. _`reference implementation`: https://github.com/alavrik/piqi-erlang/blob/f673c7dd02f4dcd52f1a0943ea5d0705262fb8fb/src/piqi_tools.erl#L106
.. _`piqi mailing list`: http://groups.google.com/group/piqi?pli=1
