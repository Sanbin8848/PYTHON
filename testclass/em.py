class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstName = firstname
        self.lastName = lastname
        self.Salary = salary

    def give_raise(self, salary_rise=5000):
        self.Salary += salary_rise


