attempts = 3
counter = 1

while counter <= attempts:
    print(f"Attempt {counter}/{attempts}")
    employee_name = input("Employee name: ")

    if employee_name.lower() == "michael":
        print("Hello, world's best boss!")
        break

    counter += 1
