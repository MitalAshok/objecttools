import unittest

from objecttools.cached_property import *


class TestCachedProperty(unittest.TestCase):
    def test_cache(self):
        get_access = []

        class Test(object):
            @CachedProperty
            def x(self):
                """dummy doc"""
                get_access.append(True)
                return 1

        t = Test()
        self.assertEqual(t.x, 1, 'Incorrect result from property cache!')
        self.assertEqual(t.x, 1, 'Incorrect result from property cache!')
        self.assertEqual(len(get_access), 1, 'Accessed too many times!')

    def test_no_set(self):
        class Test(object):
            @CachedProperty
            def x(self):
                """dummy doc"""
                return 1

        t = Test()
        with self.assertRaises(AttributeError):
            t.x = 2
        self.assertEqual(t.x, 1, 'Incorrectly set read-only property!')

    def test_no_del(self):
        class Test(object):
            @CachedProperty
            def x(self):
                return 1

        t = Test()
        with self.assertRaises(AttributeError):
            del t.x

    def test_with_del(self):
        get_access = []

        class Test(object):
            @CachedProperty
            def x(self):
                """dummy doc"""
                get_access.append(True)
                return len(get_access)

            @x.deleter
            def x(self):
                pass

        t = Test()
        self.assertEqual(t.x, 1, 'Did not call getter properly')
        self.assertEqual(t.x, 1, 'Did not cache properly')
        del t.x
        self.assertEqual(t.x, 2, 'Did not invalidate cache properly')
        self.assertEqual(t.x, 2, 'Did not cache after deleting')
        self.assertEqual(len(get_access), 2, 'Unexpected usage of getter')

    def test_with_set(self):
        get_access = []

        class Test(object):
            @CachedProperty
            def x(self):
                """dummy doc"""
                get_access.append(True)
                return len(get_access)

            @x.setter
            def x(self, value):
                pass

        t = Test()
        self.assertEqual(t.x, 1, 'Did not call getter properly')
        self.assertEqual(t.x, 1, 'Did not cache properly')
        t.x = 12
        self.assertEqual(t.x, 12, 'Did not set cache properly')
        self.assertEqual(t.x, 12, 'Did not get cache properly')
        self.assertEqual(len(get_access), 1, 'Unexpected usage of getter')

    def test_is_cached(self):
        get_access = []

        class Test(object):
            @CachedProperty
            def x(self):
                """dummy doc"""
                get_access.append(True)
                return len(get_access)

        t = Test()
        self.assertFalse(Test.x.is_cached(t), 'is_cached is wrong before cache')
        self.assertFalse(type(t).x.is_cached(t), 'Alternate is_cached is wrong before cache')
        self.assertEqual(t.x, 1, 'Did not call getter properly')
        self.assertEqual(t.x, 1, 'Did not cache properly')
        self.assertTrue(Test.x.is_cached(t), 'is_cached is wrong after cache')
        self.assertTrue(type(t).x.is_cached(t), 'Alternate is_cached is wrong after cache')


if __name__ == '__main__':
    unittest.main()
