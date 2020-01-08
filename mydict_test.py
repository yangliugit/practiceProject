import unittest

from mydict import Dict


class TestDict(unittest.TestCase):
    def setUp(self):
        print 1 + 1

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        print d
        self.assertTrue(d)
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def tearDown(self):
        print 3 + 3

if __name__ == '__main__':
    unittest.main()
