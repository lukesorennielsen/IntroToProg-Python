# ------------------------------------------------------------------------------------------------- #
# Title: test_processing_classes
# # Description: A collection of classes for test processing
# ChangeLog: (Soren, 12/11/2024, Created Script)
# RRoot,12.1.2024,Created Script
# ------------------------------------------------------------------------------------------------- #
import tempfile
import unittest
import json


from data_classes import Employee
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.temp_file=tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name

    def tearDown(self):
        self.temp_file.close()
    def test_read_data_from_file(self):
        sample_data=[
            {"FirstName": "John", "LastName": "Doe", "ReviewDate": "2030-01-01", "ReviewRating": 5},
            {"FirstName": "Soren", "LastName": "Nielsen", "ReviewDate": "2020-10-10", "ReviewRating": 2}
        ]
        with open(self.temp_file_name,'w') as file:
            json.dump(sample_data, file)
        employees: list = []
        FileProcessor.read_employee_data_from_file(self.temp_file_name,employees,Employee)

        self.assertEqual(len(sample_data), len(employees))
        self.assertEqual(sample_data[0]["FirstName"],employees[0].first_name)
        self.assertEqual(sample_data[0]["LastName"], employees[0].last_name)
        self.assertEqual(sample_data[0]["ReviewDate"], employees[0].review_date)
        self.assertEqual(sample_data[0]["ReviewRating"], employees[0].review_rating)

        self.assertEqual(sample_data[1]["FirstName"],employees[1].first_name)
        self.assertEqual(sample_data[1]["LastName"], employees[1].last_name)
        self.assertEqual(sample_data[1]["ReviewDate"], employees[1].review_date)
        self.assertEqual(sample_data[1]["ReviewRating"], employees[1].review_rating)



if __name__ == '__main__':
    unittest.main()