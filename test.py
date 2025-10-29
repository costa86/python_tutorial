import types

employee = {"name": "jim", "age": 35}
employee = types.MappingProxyType(employee)

print(
    employee, employee["age"], type(employee)
)  # => {'name': 'jim', 'age': 35} 35 <class 'mappingproxy'>
