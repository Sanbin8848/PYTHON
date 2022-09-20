import unittest
from em import Employee


class TestEmployee(unittest.TestCase):

    # def __init__(self, mye):
    #     unittest.TestCase.__init__(self)
    #     self.mye = mye

    def setUP(self):
        firstname = 'Xian_ping'
        lastname = 'Li'
        salary = 50000
        self.mye = Employee(firstname, lastname, salary)

    def test_give_default_raise(self):
        self.mye.give_raise()
        self.assertEqual(55000, self.mye.Salary)

    def test_give_custom_raise(self):
        self.mye.give_raise(6000)
        self.assertEqual(61000, self.mye.Salary)


if __name__ == 'main':
    unittest.main()
