#!/usr/bin/python3
'''
This test is for my base model. It mainly checks
    - to_dict
    - save
    - str
'''
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''Tests My model to validate the instance will be created successfully'''
    def setUp(self):
        '''Its essential to avoid creating multiple test data in every test'''
        self.my_object = BaseModel()
        
    def test_init(self):
        '''Test that object is correctly created'''
        self.assertIs(type(self.my_object), BaseModel)
        self.assertIsInstance(self.my_object.created_at, datetime)
        self.assertIsInstance(self.my_object.updated_at, datetime)
    
    def test_save(self):
        '''Checks if the save method updates the time of modification'''
        initial = self.my_object.updated_at
        # Call the save method
        self.my_object.save()
        # Check if the updated time value has changed
        self.assertNotEqual(initial, self.my_object.updated_at)
    
    def test_to_dict(self):
        '''Tests the to_dict to confirm it returns a dictionary, with the sppecifications'''
        # Check if to_dict returns a dictionary
        self.assertIsInstance(self.my_object.to_dict(), dict) 
        
        # Check if the class key is present in the dict
        self.assertIn('__class__', self.my_object.to_dict())
        
        # Check if created_at and updated_at are in ISO format
        iso_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(
            datetime.strptime(self.my_object.to_dict()['created_at'], iso_format),
            self.my_object.created_at
        )
        self.assertEqual(
            datetime.strptime(self.my_object.to_dict()['updated_at'], iso_format),
            self.my_object.updated_at
        )



if __name__ == "__main__":
    unittest.main() 