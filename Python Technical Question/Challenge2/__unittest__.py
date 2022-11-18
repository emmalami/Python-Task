import unittest
import task1a

class TestAdd(unittest.TestCase):
    def test_add(self):
        result = task1a.add(5, 5)
        self.assertEqual(result, 10)



if __name__ == '__name__':
    unittest.main()