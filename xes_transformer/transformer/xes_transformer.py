import unittest
from xes import *


traces = [
    [
        {"concept:name": "Register", "org:resource": "Bob"},
        {"concept:name": "Negotiate", "org:resource": "Sally"},
        {"concept:name": "Negotiate", "org:resource": "Sally"},
        {"concept:name": "Sign", "org:resource": "Dan"},
        {"concept:name": "Sendoff", "org:resource": "Mary"}
    ],
    [
        {"concept:name": "Register", "org:resource": "Bob"},
        {"concept:name": "Negotiate", "org:resource": "Sally"},
        {"concept:name": "Sign", "org:resource": "Dan"},
        {"concept:name": "Sendoff", "org:resource": "Mary"}
    ],
    [
        {"concept:name": "Register", "org:resource": "Bob"},
        {"concept:name": "Negotiate", "org:resource": "Sally"},
        {"concept:name": "Sign", "org:resource": "Dan"},
        {"concept:name": "Negotiate", "org:resource": "Sally"},
        {"concept:name": "Sendoff", "org:resource": "Mary"}
    ],
    [
        {"concept:name": "Register", "org:resource": "Bob"},
        {"concept:name": "Sign", "org:resource": "Dan"},
        {"concept:name": "Sendoff", "org:resource": "Mary"}
    ]
]


def first_method():
    return True


def convert_xes_example():
    doc = XESDocument()

    trace1 = Trace()
    trace1.addAttribute(Attribute("string", "concept:name", "1"))
    trace1.addEvent(Event().addAttribute(Attribute("string", "org:resource", "Rose")))
    trace1.addEvent(Event().addAttribute(Attribute("string", "lifecycle:transition", "start")))

    trace2 = Trace()
    trace2.addAttribute(Attribute("string", "concept:name", "2"))
    trace2.addEvent(Event().addAttribute(Attribute("string", "org:resource", "Bob")))
    trace2.addEvent(Event().addAttribute(Attribute("string", "lifecycle:transition", "start")))

    doc.addAttribute(Attribute("something", "or", "other"))
    doc.addTrace(trace1)
    doc.addTrace(trace2)

    print doc
    return doc


class TestXesTransformer(unittest.TestCase):
    def test_first_method(self):
        print "Do you know where your towel is?"
        self.assertTrue(first_method())

    def test_convert_xes(self):
        self.assertTrue(convert_xes_example())


if __name__ == '__main__':
    unittest.main()