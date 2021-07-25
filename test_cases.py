from main import json_to_db
import unittest


class TestJsonToDbMethods(unittest.TestCase):

    def test_invalid_json(self):
        self.assertRaises(Exception, json_to_db, 'errorjson.json')

    def test_file_not_exist(self):
        self.assertRaises(Exception, json_to_db, '.json')

    def test_wrong_json(self):
        self.assertRaises(Exception, json_to_db, 'wrongformat.json')

    def test_ok(self):
        self.assertIsNone(json_to_db('sample.json'))


if __name__ == '__main__':
    unittest.main()
