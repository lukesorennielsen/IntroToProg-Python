# ------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# ------------------------------------------------------------------------------- #
import unittest
import tempfile
import json
import data_classes as data
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.student_data = []

    def tearDown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()

    def test_read_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "John", "LastName": "Doe", "GPA": 3.5},
            {"FirstName": "Alice", "LastName": "Smith", "GPA": 3.8},
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_data_from_file method and check if it returns the expected data
        FileProcessor.read_data_from_file(self.temp_file_name, self.student_data)

        # Assert that the student_data list contains the expected student objects
        self.assertEqual(len(self.student_data), len(sample_data))
        self.assertEqual(self.student_data[0].first_name, "John")
        self.assertEqual(self.student_data[1].gpa, 3.8)

    def test_write_data_to_file(self):
        # Create some sample student objects
        sample_students = [
            data.Student("John", "Doe", 3.5),
            data.Student("Alice", "Smith", 3.8),
        ]

        # Call the write_data_to_file method to write the data to the temporary file
        FileProcessor.write_data_to_file(self.temp_file_name, sample_students)

        # Read the data from the temporary file and check if it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_students))
        self.assertEqual(file_data[0]["FirstName"], "John")
        self.assertEqual(file_data[1]["GPA"], 3.8)

if __name__ == "__main__":
    unittest.main()