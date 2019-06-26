import unittest
from flask_app import app



class TestGetAccount(unittest.TestCase):
    def setUp(self):
        self.client = app.create_account("John Smith", 100, "plan_B")
        # self.client = app.test_client()
        # with app.app_context():
        # ...

    def test_existing_account(self):
        r = self.client.get("/accounts/1", {})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json["client_name"], "John Doe")
        self.assertEqual(r.json["credits"], 125.001)

    def test_inexisting_account(self):
        r = self.client.get("/accounts/123123789", {})
        self.assertEqual(r.status_code, 404)

    def test_invalid_ids_account(self):
        invalid = [None, 123.23, True, "drop database",]
        for v in invalid:
            r = self.client.get("/accounts/%s" % v, {})
            self.assertEqual(r.status_code, 404)