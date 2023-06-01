import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.meng = Employee('mengli', 'gu', 1000)
    
    def test_give_default_raise(self):
        self.meng.give_raise()
        self.assertEqual(self.meng.salary, 6000)

    def test_give_custom_raise(self):
        self.meng.give_raise(2000)
        self.assertEqual(self.meng.salary, 1000+2000)


if __name__ == '__main__':
    unittest.main()