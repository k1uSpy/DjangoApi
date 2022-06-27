from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Contacts

# Create your tests here.

class TestContacts(APITestCase):
    
    url = "/contact"

    def setUp(self):
        #definition
        Contacts.objects.create(ContactName="Daniel", ContactPhone="0742324124", ContactAddress="dwqd@gmail.com")

    def test_get_contacts(self):
        
        #process
        response = self.client.get(self.url)
        result = response.json()
        
        #assert

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["ContactName"], "Daniel")

    def test_post_contacts(self):
        contact_data = {
            "ContactName": "Mircea",
            "ContactPhone": "0756234123",
            "ContactAddress": "dwqd@gmail.com"
            }
        response = self.client.post(self.url, data=contact_data)

        self.assertEqual(response.status_code, 201)

   

