import unittest
from app.validator import Validate
from app.simulators import UserNotFoundException, User, Users, NullUserError


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
            "absent_key": ""
        }
        rules = {"absent_key": {
            "required": True
        }}
        self.assertRaises(KeyError, self.validator.validate_data,
                          source=form_data, items=rules)

    def test_unique_email_on_registration(self):
        pass

    def test_invalid_email_from_form(self):
        pass


class UserSimulatorTestCases(unittest.TestCase):
    def setUp(self):
        self.user = User("brian","os","python@php.org","password@1")
        self.users = Users()

    def test_access_of_inexistent_user(self):
        self.assertRaises(UserNotFoundException, self.users.get_user, 7)

    def test_new_empty_user_addition(self):
        self.assertRaises(NullUserError, self.users.add_user, {})

    def test_users_increment_when_a_user_is_added(self):
        users_len = len(self.users.users)
        self.users.add_user({"firstname": "dennis", "lastname": "Deilson",
                             "email": "denilson@gmail.com", "password": "password"})
        new_users_len = len(self.users.users)
        self.assertEqual(users_len+1, new_users_len)

    def test_user_absence_on_deletion(self):
        self.users.delete_user(1)
        self.assertFalse("1" in self.users.users)

    def test_raise_user_not_found_exception_if_user_is_deleted(self):
        self.assertRaises(NullUserError, self.users.delete_user, 7)


if __name__ == "__main__":
    unittest.main()
