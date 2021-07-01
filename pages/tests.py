from django.http import response
from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    
    def test_reading_page_status_code(self):
        response = self.client.get('/reading/')
        self.assertEqual(response.status_code, 200)

        
    def test_mass_page_status_code(self):
        response = self.client.get('/mass/')
        self.assertEqual(response.status_code, 200)

    
    def test_bulletin_page_status_code(self):
        response = self.client.get('/bulletin/')
        self.assertEqual(response.status_code, 200)
