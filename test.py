from app import app
import unittest


class TestCalculator(unittest.TestCase):

    def test_add(self):
        with app.test_client() as c:
            response = c.get('/add?a=2&b=2')
            self.assertIn(b'4', response.data)
            self.assertEqual(response.status_code, 200)

    def test_subtract(self):
        with app.test_client() as c:
            response = c.get('/sub?a=2&b=2')
            self.assertIn(b'0', response.data)
            self.assertEqual(response.status_code, 200)

    def test_multiply(self):
        with app.test_client() as c:
            response = c.get('/mult?a=20&b=2')
            self.assertIn(b'40', response.data)
            self.assertEqual(response.status_code, 200)

    def test_division(self):
        with app.test_client() as c:
            response = c.get('/div?a=2&b=2')
            self.assertIn(b'1', response.data)
            self.assertEqual(response.status_code, 200)

    def test_all_in_one(self):
        with app.test_client() as c:
            response = c.get('/math/add?a=2&b=2')
            self.assertIn(b'4', response.data)
            self.assertEqual(response.status_code, 200)

            response = c.get('/math/sub?a=2&b=2')
            self.assertIn(b'0', response.data)
            self.assertEqual(response.status_code, 200)

            response = c.get('/math/mult?a=20&b=2')
            self.assertIn(b'40', response.data)
            self.assertEqual(response.status_code, 200)

            response = c.get('/math/div?a=2&b=2')
            self.assertIn(b'1', response.data)
            self.assertEqual(response.status_code, 200)
