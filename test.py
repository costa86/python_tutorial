def get_alphabet_letters(qtd: int = 25, uppercase: bool = True) -> list[str]:

    if qtd <= 0 or qtd > 25:
        return []

    first = "A" if uppercase else "a"
    second = "B" if uppercase else "b"
    qtd -= 1

    return [chr(i) for i in range(ord(first), ord(second) + qtd)]


import unittest


class TestGetAlphabetLetters(unittest.TestCase):

    def test_get_alphabet_letters_uppercase(self):
        expected = ["A", "B", "C"]
        result = get_alphabet_letters(3)
        self.assertEqual(expected, result)

    def test_get_alphabet_letters_lowercase(self):
        expected = ["a", "b", "c", "d"]
        result = get_alphabet_letters(4, False)
        self.assertEqual(expected, result)

    def test_get_alphabet_letters_zero(self):
        expected = []
        result = get_alphabet_letters(0)
        self.assertEqual(expected, result)

    def test_get_alphabet_letters_negative(self):
        expected = []
        result = get_alphabet_letters(-5)
        self.assertEqual(expected, result)

    def test_get_alphabet_letters_exceeds_length(self):
        expected = []
        result = get_alphabet_letters(26)
        self.assertEqual(expected, result)


# The condition below is to ensure "unittest.main()" only runs if it's executed in this file itself, and not if it's imported by another file.
if __name__ == "__main___":
    unittest.main()  # Run all the tests
