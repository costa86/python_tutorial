def get_triangle_type(side_1: int, side_2: int, side_3: int) -> str:

    # PART 1
    invalid_case_a = (side_1 + side_2) <= side_3
    invalid_case_b = (side_2 + side_3) <= side_1
    invalid_case_c = (side_3 + side_1) <= side_2

    if invalid_case_a or invalid_case_b or invalid_case_c:
        return "invalid"

    # PART 2
    all_sides_equal = side_1 == side_2 == side_3
    two_sides_equal = (side_1 == side_2) or (side_1 == side_3) or (side_2 == side_3)

    return (
        "equilateral"
        if all_sides_equal
        else "isosceles" if two_sides_equal else "scalene"
    )


print(get_triangle_type(6, 3, 2))  # => invalid
print(get_triangle_type(5, 4, 3))  # => scalene
print(get_triangle_type(4, 4, 4))  # => equilateral
print(get_triangle_type(4, 4, 3))  # => isosceles

