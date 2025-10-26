class Product:
    # See about “pass” in the Error/Exception handling chapter. For now, think of it as just a placeholder without any action.
    pass


class Beet(Product):
    """
    From Schrute farms
    """

    pass


class Printer(Product):
    """
    From Saber company
    """

    pass


class Paper(Product):
    """
    From Dunder Mifflin company
    """

    pass


class SalesPerson:
    """
    I sell many products
    """

    def __init__(self, name: str, products: list[Product]):
        self.name = name
        self.products = products


jim = SalesPerson("Jim", [Paper, Printer])
dwight = SalesPerson("Dwight", [Paper, Printer, Beet])

print("Jim", [i.__name__ for i in jim.products])  # => Jim ['Paper', 'Printer']
print(
    "Dwight", [i.__name__ for i in dwight.products]
)  # => Dwight ['Paper', 'Printer', 'Beet']
