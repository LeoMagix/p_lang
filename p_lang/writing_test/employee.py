#Practice program to test written code:
class EmployeePay:
    """Increase pay for employees."""

    def __init__(self, first_name, last_name, annual_salary=2000):
        """Receive employee name, increase their salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, pay_raise=5000):
        """
        Increases the current pay by default with $5000.
        However, allows for a customised pay raise.
        """
        formatted_name = f'{self.first_name} {self.last_name}'
        new_pay = pay_raise + self.annual_salary
        msg = f"{formatted_name.title()}, your annual salary is now ${new_pay}."
        return msg
