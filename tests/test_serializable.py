import unittest
import pickle

from objecttools.serializable import *


class DummyClass(object):
    def method(self):
        return self.__class__.__name__

    def unpicklable(self):
        def inner_func(a):
            return self.__class__.__name__[:a]

        return inner_func

dummy = DummyClass()
unpicklable = dummy.unpicklable()


class TestSerializable(unittest.TestCase):
    def test_serializable_functions(self):
        def function(a):
            return a + 1

        anonymous = lambda a: a + 2
        bound_method = dummy.method
        unbound_method = DummyClass.method

        s_function = SerializableFunction(function)
        s_anonymous = SerializableFunction(anonymous)
        s_bound_method = SerializableFunction(bound_method)
        s_unbound_method = SerializableFunction(unbound_method)

        expected = bound_method()

        for i in range(3):
            m = ' ({})'.format(i) if i else ''
            self.assertIsNot(s_function.value, function, 'Erroneously returned same object' + m)
            self.assertEqual(s_function.value(1), 2, 'Wrong reconstruction of value' + m)
            self.assertEqual(s_function(1), 2, 'Wrong __call__ when serialized' + m)
            self.assertEqual(s_anonymous(1), 3, 'Wrong reconstruction of <lambda>' + m)
            self.assertEqual(s_bound_method(), expected, 'Wrong reconstruction of bound method' + m)
            self.assertEqual(s_unbound_method(dummy), expected, 'Wrong reconstruction of unbound method' + m)
            s_function = pickle.loads(pickle.dumps(s_function))
            s_anonymous = pickle.loads(pickle.dumps(s_anonymous))
            s_bound_method = pickle.loads(pickle.dumps(s_bound_method))
            s_unbound_method = pickle.loads(pickle.dumps(s_unbound_method))

    def test_serializable_constant(self):
        const = SerializableConstant('unpicklable', __name__)
        self.assertIs(const.value, unpicklable, 'Constant objects are different')
        with self.assertRaises(AttributeError):
            self.assertIsInstance(pickle.dumps(unpicklable), type(b''))
        expected = unpicklable(1)
        self.assertEqual(pickle.loads(pickle.dumps(const))(1), expected, 'Constant object is wrong after pickling')


if __name__ == '__main__':
    unittest.main()
