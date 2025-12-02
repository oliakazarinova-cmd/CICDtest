import unittest
# src/tests.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import app as tested_app
import json

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_add_success(self):
        r = self.app.get('/add?a=2&b=3')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'5.0')
    
    def test_dec_success(self):
        r = self.app.get('/dec?a=10&b=6')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'4.0')
##
###
if __name__ == '__main__':
    unittest.main()