import unittest
from employee import EmployeePay as EP

class TestEmployeeRaise(unittest.TestCase):
    """Test for EmployeePay class."""

    def setUp(self):
        """Make available annual salary to all test case."""
        self.annual_salary = 2000
        self.worker = EP('james', 'oblah', self.annual_salary)

    def test_give_default_raise(self):
        """Adds $5000 to the annual salary by default."""
        msg = 'James Oblah, your annual salary is now $7000.'
        pay = self.worker.give_raise()
        self.assertEqual(pay, msg)

    def test_give_custom_raise(self):
        """Customize your workers pay increase."""
        increase = 8000
        new = self.annual_salary + increase 
        custom_pay = self.worker.give_raise(increase)
        msg = f'James Oblah, your annual salary is now ${new}.'
        self.assertEqual(custom_pay, msg)


if __name__ == '__main__':
    unittest.main()
