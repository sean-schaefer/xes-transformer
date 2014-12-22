import unittest


def first_method():
    return True


class TestXesTransformer(unittest.TestCase):
    def test_first_method(self):
        print "Do you know where your towel is?"
        self.assertTrue(first_method())


if __name__ == '__main__':
    unittest.main()