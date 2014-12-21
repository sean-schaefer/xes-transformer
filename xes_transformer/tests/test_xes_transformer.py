import unittest
from xes_transformer.transformer import xes_transformer


class TestXesTransformer(unittest.TestCase):
    def test_first_method(self):
        print "Do you know where your towel is?"
        self.assertTrue(xes_transformer.first_method())