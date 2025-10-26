class Employee:
    def __init__(self):
        self.company = "Dunder Mifflin"
        self.salary = 0.0

    def promote(self, salary_raise: float) -> float:
        self.salary += salary_raise
        return self.salary


class Singer:
    def __init__(self):
        self.instrument = "Banjo"


class SalesPerson(Employee, Singer):
    def __init__(self):
        Employee.__init__(self)
        Singer.__init__(self)


sales_person = SalesPerson()

all_available = dir(sales_person)

all_properties = vars(sales_person)

all_methods = [
    i
    for i in dir(sales_person)
    if callable(getattr(sales_person, i)) and not i.startswith("__")
]

print("Everything available", all_available)
print("All the properties", all_properties)
print("All the methods", all_methods)
