import unittest

from objecttools.object_proxy import *


class TestObjectProxy(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(ObjectProxy(1), 1)
        self.assertEqual([ObjectProxy(1)], [1])
        self.assertEqual(ObjectProxy(1.), 1)

    def test_hash(self):
        with self.assertRaises(TypeError):
            self.assertFalse({ObjectProxy([])})
        self.assertEqual(hash(ObjectProxy(1)), hash(1), 'hash unequal')
        self.assertEqual(len({ObjectProxy(1), 1}), 1, 'hash or eq not equal in sets')

    def test_no_identity(self):
        test = object()
        self.assertNotEqual(id(ObjectProxy(test)), id(test), 'id the same')
        self.assertIsNot(ObjectProxy(test), test, 'is the same')
        self.assertIsNot(ObjectProxy(test), ObjectProxy(test), 'different ObjectProxy are the same')

    def test_bool(self):
        self.assertTrue(ObjectProxy(1))
        self.assertTrue(ObjectProxy([1]))
        self.assertFalse(ObjectProxy(0))
        self.assertFalse(ObjectProxy([]))

    def test_attributes(self):
        d = {1: 1, 2: 1}
        self.assertEqual(set(ObjectProxy(d).keys()), set(d.keys()))
        self.assertEqual(ObjectProxy('a').upper(), 'A')
