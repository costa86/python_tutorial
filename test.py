class Father:
    def __init__(self):
        self.eye_color = "green"


class Mother:
    def __init__(self):
        self.hair_color = "black"


class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)


child = Child()

print(child.hair_color)
print(child.eye_color)
print(Child.mro())
