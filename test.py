def get_multiple_named_parameters(**kwargs):
    return kwargs


a = get_multiple_named_parameters(name="Ryan", age=25)
b = get_multiple_named_parameters(code=2, color="red", active=False)

print(a)  # => {'name': 'Ryan', 'age': 25}
print(b)  # => {'code': 2, 'color': 'red', 'active': False}
print(type(a), type(b))  # => <class 'dict'> <class 'dict'>
