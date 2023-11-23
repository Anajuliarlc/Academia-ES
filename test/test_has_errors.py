import unittest

import sys 
import os
sys.path.append(os.path.abspath("./src")) # Adds src directory to python modules path.

import student.register_card as rc
import exc.exceptions as exc

class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        pass

    # Name tests
    def test_none_name(self) -> None:
        self.assertRaises(exc.EmptyFieldError, rc.has_errors, None, "1234123412341234", "Crédito", "12/12", "123")

    def test_empty_name(self) -> None:
        self.assertRaises(exc.EmptyFieldError, rc.has_errors, "", "1234123412341234", "Crédito", "12/12", "123")

    def test_wrong_name_type(self) -> None:
        self.assertRaises(exc.WrongTypeError, rc.has_errors, 123, "1234123412341234", "Crédito", "12/12", "123")

    def test_name_contains_non_letters(self) -> None:
        self.assertRaises(exc.NonLetterError, rc.has_errors, "123", "1234123412341234", "Crédito", "12/12", "123")

    # Number tests
    def test_none_number(self) -> None:
        self.assertRaises(exc.EmptyFieldError, rc.has_errors, "Nome", None, "Crédito", "12/12", "123")

    def test_number_is_not_int(self) -> None:
        self.assertRaises(exc.WrongTypeError, rc.has_errors, "Nome", "abc", "Crédito", "12/12", "123")

    def test_number_length_is_not_16(self) -> None:
        self.assertRaises(exc.WrongLengthError, rc.has_errors, "Nome", 1234, "Crédito", "12/12", "123")

    # Card type tests
    def test_card_type_is_not_string(self) -> None:
        self.assertRaises(exc.WrongTypeError, rc.has_errors, "Nome", 1234123412341234, 123, "12/12", "123")

    def test_invalid_card_type(self) -> None:
        self.assertRaises(exc.InvalidCardTypeError, rc.has_errors, "Nome", 1234123412341234, "invalid", "12/12", "123")

    # Date tests
    def test_date_is_not_string(self) -> None:
        self.assertRaises(exc.WrongTypeError, rc.has_errors, "Nome", 1234123412341234, "Crédito", 12, "123")

    def test_date_length_is_not_5(self) -> None:
        self.assertRaises(exc.WrongLengthError, rc.has_errors, "Nome", 1234123412341234, "Crédito", "123", "123")

    def test_middle_date_slash_is_missing(self) -> None:
        self.assertRaises(exc.WrongFormatError, rc.has_errors, "Nome", 1234123412341234, "Crédito", "12-12", "123")

    def test_non_numerical_date(self) -> None:
        self.assertRaises(exc.WrongTypeError, rc.has_errors, "Nome", 1234123412341234, "Crédito", "ab/cd", "123")

    # CVV tests
    def test_cvv_is_not_int(self) -> None:
        self.assertRaises(exc.WrongTypeError, rc.has_errors, "Nome", 1234123412341234, "Crédito", "12/12", "abc")

    def test_cvv_length_is_not_3(self) -> None:
        self.assertRaises(exc.WrongLengthError, rc.has_errors, "Nome", 1234123412341234, "Crédito", "12/12", 1234)

if __name__ == "__main__":
    unittest.main()
