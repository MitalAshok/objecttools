if __name__ == '__main__':
    import unittest
    import os
    import sys

    __dir__ = os.path.abspath(os.path.dirname(__file__))

    sys.path.insert(0, os.path.dirname(__dir__))

    try:
        from tests.test_singletons import TestSingletons
        from tests.test_cached_property import TestCachedProperty
        from tests.test_object_proxy import TestObjectProxy
        from tests.test_serializable import TestSerializable
    finally:
        sys.path.pop(0)

    unittest.main()
