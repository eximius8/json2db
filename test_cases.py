from main import json_to_db
import unittest


class TestJsonToDbMethods(unittest.TestCase):

    def test_invalid_json(self):
        self.assertRaises(Exception, json_to_db, './tests/errorjson.json')

    def test_file_not_exist(self):
        self.assertRaises(Exception, json_to_db, '.json')

    def test_wrong_json(self):
        self.assertRaises(Exception, json_to_db, './tests/wrongformat.json')

    def test_ok(self):
        self.assertIsNone(json_to_db('./tests/sample.json'))


if __name__ == '__main__':
    unittest.main()
