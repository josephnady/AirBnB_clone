#!/usr/bin/python3
import os

from models.engine.file_storage import FileStorage
import models
import unittest
import json


class TestFileStorage(unittest.TestCase):
    """test case for File Storage"""

    def setUp(self):
        """Setup func that start before each test"""
        self.storage = FileStorage()

    def tearDown(self):
        """tearDown func that start after each test"""
        if os.path.isfile('file.json'):
            os.remove('file.json')

    def test_new_instance(self):
        """Doc"""
        """test if new instance is created"""
        self.assertEqual(self.storage.__class__.__name__, "FileStorage")

    def test__file_path(self):
        """Doc"""
        storage = FileStorage()
        filepath = storage._FileStorage__file_path
        self.assertEqual(filepath, 'file.json')

    def test_FileStorage__objects(self):
        """Doc"""
        storage = FileStorage()
        objects = storage._FileStorage__objects
        self.assertEqual(type(objects), dict)

    def test_storage_new_instance(self):
        """test storage new Instance"""
        storage = FileStorage()
        save = storage._FileStorage__objects
        new_dict = self.storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, save)

    def test_all(self):
        """"test all() function in FileStorage Class"""
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """"test new() function in FileStorage Class"""
        storage = FileStorage()
        save = storage._FileStorage__objects
        storage._FileStorage__objects = {}
        test_dict = {}
        for key, value in models.classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertNotEqual(test_dict, storage._FileStorage__objects)
        storage._FileStorage__objects = save

    def test_reload(self):
        """"test reload() function in FileStorage Class"""
        self.assertIsNone(self.storage.reload())

    def test_save(self):
        """"test the save() function in FileStorage Class"""
        storage = FileStorage()
        new_dict = {}
        for key, value in models.classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))


if __name__ == "__main__":
    unittest.main()
