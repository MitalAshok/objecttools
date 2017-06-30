import unittest

from objecttools.singletons import *


@Singleton.as_decorator
class Test(object):
    pass


class TestSingletons(unittest.TestCase):
    def test_identity(self):
        a = Test()
        b = Test()
        self.assertIs(a, b)

    def test_subclass_identity(self):
        class TestB(Test):
            pass

        @Singleton.as_decorator
        class TestC(Test):
            pass

        a = Test()
        b = TestB()
        c = TestC()
        self.assertIs(a, b)
        self.assertIs(a, c)
        self.assertIs(b, c)

    def test_representation(self):
        singleton = Singleton.create('Singleton', object_name='singleton')()
        self.assertEqual(repr(singleton), 'singleton', 'Instance not assigned proper __repr__')
        self.assertEqual(repr(type(singleton)), 'Singleton', 'Class not assigned proper __repr__')

if __name__ == '__main__':
    unittest.main()
