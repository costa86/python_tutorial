from enum import Enum


class JobPosition(Enum):  # An enum is a class
    SALESPERSON = "salesperson"
    REGIONAL_MANAGER = "regional manager"
    ACCOUNTANT = "accountant"


introduction = f"Kevin is an {JobPosition.ACCOUNTANT.value}"
print(introduction)  # => Kevin is an accountant
