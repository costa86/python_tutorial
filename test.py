def get_employees_by_department(department: str) -> list:

    match department.lower():

        case "sales":
            return ["jim", "dwight", "phyllis", "stanley"]

        case "accounting":
            return ["angela", "oscar", "kevin"]

        case "human resources" | "human_resources":  # either one
            return ["toby"]

        case "reception":
            return ["pam"]

        return []


print(get_employees_by_department("human_resources"))  # => ['toby']
print(get_employees_by_department("ccounting"))  # => ['angela', 'oscar', 'kevin']
print(get_employees_by_department("management"))  # => []
