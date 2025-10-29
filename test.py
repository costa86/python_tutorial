from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int

    def get_info(self) -> str:
        return f"Employee: {self.name}, Age: {self.age}"


class Manager(Employee):
    branch: str


class Singer(BaseModel):
    genre: str

    def sing(self) -> str:
        return f"I sing {self.genre} music."


class SalesPerson(Employee, Singer):
    department: str

    def make_sale(self) -> str:
        return f"{self.name} from {self.department} made a sale."


class JuniorSalesPerson(SalesPerson):
    supervisor: str

    def report_to_supervisor(self) -> None:
        print(f"{self.name} is reporting to {self.supervisor}.")
