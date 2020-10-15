import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual('foo'.upper(),'FOO')

    def test_isupper(self):
        self.assertEqual('FOO'.isupper())
        self.assertEqual('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
