# ------------------------------------------------------------------------------------------------- #
# Title: test_data_classes
# # Description: A collection of classes for test data
# ChangeLog: (Soren, 12/11/2024, Created Script)
# RRoot,12.1.2024,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest


from data_classes import Person,Employee


class TestPerson(unittest.TestCase):
    def test_person_init(self):
        person = Person("vic","vu")
        self.assertEqual("Vic", person.first_name)
        self.assertEqual("Vu", person.last_name)

    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):
            person=Person("vic","456")
        with self.assertRaises(ValueError):
            person = Person("123", "vu")

    def test_person_str(self):
        person = Person("Vic","Vu")
        self.assertEqual("Vic,Vu",str(person))

class TestEmployee(unittest.TestCase):
    def test_employee_init(self):
        employee=Employee("Vic","Vu","1900-01-01",5)
        self.assertEqual("Vic,Vu,1900-01-01,5", str(employee))
        self.assertEqual("Vic",employee.first_name)
        self.assertEqual("Vu", employee.last_name)
        self.assertEqual("1900-01-01", employee.review_date)
        self.assertEqual(5, employee.review_rating)

    def test_employee_date(self):
        with self.assertRaises(ValueError):
            employee =Employee("Vic","Vu","March 2021",5)
    def test_employee_rating(self):
        with self.assertRaises(ValueError):
            employee = Employee("Vic","Vu","1900-01-01","Five")

if __name__ == '__main__':
    unittest.main()
