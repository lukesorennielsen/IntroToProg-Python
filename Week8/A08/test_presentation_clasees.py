# ------------------------------------------------------------------------------------------------- #
# Title: test_presentation_classes
# # Description: A collection of classes for test presentation
# ChangeLog: (Soren, 12/11/2024, Created Script)
# RRoot,12.1.2024,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest


from data_classes import Employee
from presentation_classes import IO
from unittest.mock import patch

class TestIOProcessor(unittest.TestCase):
    def test_get_input(self):
        with patch("builtins.input",return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual("2",choice)

    def test_input_employee_data(self):
        with patch("builtins.input",side_effect=["Vic","Vu","1900-01-01","5"]):
            employees=[]
            IO.input_employee_data(employees,Employee)
            self.assertEqual(1,len(employees))
            self.assertEqual("Vic",employees[0].first_name)
            self.assertEqual("Vu", employees[0].last_name)
            self.assertEqual("1900-01-01", employees[0].review_date)
            self.assertEqual(5, employees[0].review_rating)
    def test_input_employee_data_invalid_date(self):
        with patch("builtins.input", side_effect=["Vic", "Vu", "september ninth 1900", "5"]):
            employees = []
            IO.input_employee_data(employees, Employee)
            self.assertEqual(0, len(employees))

if __name__ == '__main__':
    unittest.main()