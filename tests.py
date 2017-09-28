import unittest
from app.validator import Validate


class ValidationTestCases(unittest.TestCase):
    def setUp(self):
        self.validator = Validate()

    def test_empty_required_form_field(self):
        form_data = {"lname": ""}
        rules = {"lname": {
            "required": True
        }}
        self.assertTrue(self.validator.validate_data(form_data, rules))

    def test_no_number_in_form_field(self):
        form_data = {"lname": "d56"}
        rules = {"lname": {
            "no_number": True
        }}
        self.assertTrue(self.validator.validate_data(form_data, rules))

    def test_min_length_of_form_input(self):
        form_data = {"lname": "den"}
        rules = {"lname": {
            "min": 6
        }}
        self.assertTrue(self.validator.validate_data(form_data, rules))

    def test_max_length_of_form_input(self):
        form_data = {"lname": "denhhhhh"}
        rules = {"lname": {
            "max": 6
        }}
        self.assertTrue(self.validator.validate_data(form_data, rules))

    def test_invalid_key_from_form(self):
        form_data = {
            "absent_key": "people"
        }
        rules = {"absent_key": {
            "required": True
        }}
        self.assertRaises(KeyError, self.validator.validate_data, source=form_data, items=rules)

    def test_unique_username_on_registration(self):
        pass

    def test_invalid_email_from_form(self):
        pass


if __name__ == "__main__":
    unittest.main()
