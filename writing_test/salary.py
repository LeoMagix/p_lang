from employee import EmployeePay as EP

first = input("First name: ")
last = input("Last name: ")
annual_pay = input("Annual salary: ")
salary = int(annual_pay)

worker = EP(first, last, salary)
print(worker.give_raise())
