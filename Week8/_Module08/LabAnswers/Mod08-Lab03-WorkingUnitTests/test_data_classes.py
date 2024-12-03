# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Student


class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")


class TestStudent(unittest.TestCase):

    def test_student_init(self):  # Tests the constructor
        student = Student("Alice", "Smith", 3.5)
        self.assertEqual(student.first_name, "Alice")
        self.assertEqual(student.last_name, "Smith")
        self.assertEqual(student.gpa, 3.5)

    def test_student_gpa_type(self):  # Test the gpa validation
        with self.assertRaises(ValueError):
            student = Student("Bob", "Johnson", "invalid_gpa")

    def test_student_str(self):
        student = Student("Eve", "Brown", 4.0)  # Tests the __str__() magic method
        self.assertEqual(str(student), "Eve,Brown,4.0")

if __name__ == '__main__':
    unittest.main()


