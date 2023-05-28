import unittest
import math

from Lab3.task.serialize import JSONSerializer

def my_decorator(func):
    def inner(*args, **kwargs):
        print("a")
        return func(*args, **kwargs)
    return inner

def my_gen(a):
    for i in a:
        yield i

class TestClass1:
    SOME_PROP_1 = {
        'a': None,
        'b': True,
        'c': False
    }

    @my_decorator
    def test_dec(self, a):
        return math.sin(a)

    def __init__(self, aa):
        self.a = 4
        self.aa = aa

    def test_bound_1(self):
        return self.a + self.aa

    @staticmethod
    def test_static_1(a):
        return a * 3
    
    @property
    def test_property(self):
        return self.SOME_PROP_1["a"]


class TestClass2(TestClass1):
    SOME_PROP_2 = 'ahuha2 aboba@ amuga'

    def __init__(self, bb):
        super().__init__(bb * 2)
        self.b = 5
        self.bb = bb - 0.8

    @classmethod
    def test_class_2(cls):
        return cls.SOME_PROP_1


class WithoutInheritanceCase(unittest.TestCase):
    json_ser = JSONSerializer()

    def test_gen(self):
        testing = my_gen([1, 2, 3, 4, 5])
        self.assertEqual(
            next(self.json_ser.loads(self.json_ser.dumps(testing))), next(testing)
        )   

    def test_no_inheritance(self):
        self.assertEqual(
            self.json_ser.loads(self.json_ser.dumps(TestClass1))(12).test_bound_1(),
            TestClass1(12).test_bound_1()
        )
        self.assertEqual(
            self.json_ser.loads(self.json_ser.dumps(TestClass1)).test_static_1(2),
            TestClass1.test_static_1(2)
        )

    def test_my_dec(self):
        tester = TestClass1(12)
        self.assertEqual(
            self.json_ser.loads(self.json_ser.dumps(tester)).test_dec(3), tester.test_dec(3)
        )

    def test_rab_property(self):
        tester = TestClass1(12)
        self.assertEqual(
            self.json_ser.loads(self.json_ser.dumps(tester)).test_property, tester.test_property
        )

    def test_single_class_inheritance(self):
        self.assertEqual(
            self.json_ser.loads(self.json_ser.dumps(TestClass2)).SOME_PROP_1,
            TestClass2.SOME_PROP_1
        )
        self.assertEqual(
            self.json_ser.loads(self.json_ser.dumps(TestClass2))(12).test_bound_1(),
            TestClass2(12).test_bound_1()
        )
        self.assertEqual(
            self.json_ser.loads(
                self.json_ser.dumps(TestClass2)
            ).test_class_2(self.json_ser.loads(self.json_ser.dumps(TestClass2))),
            TestClass2.test_class_2()
        )
    


if __name__ == '__main__':
    unittest.main()