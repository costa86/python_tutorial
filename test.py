class Employee:
    def __init__(self):
        self.company = "Dunder Mifflin"


class Singer:
    def __init__(self):
        self.intrument = "Banjo"


class SalesPerson(Employee, Singer):
    pass


a = SalesPerson()
print(a.company)
print(a.intrument)
