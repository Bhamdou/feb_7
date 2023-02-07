from http import HTTPStatus
from django.test import TestCase

# 200 ? Success / OK
# 404 ? Not found

class AddFeedbackFormTest(TestCase):

    def test_get(self):
        response = self.client.get("/new/")
        # assertions
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Create feedback</h1>")
        
        
    def test_post_when_successful(self):
        response = self.client.post("/new/", data={"name": "Jane Doey", "message": "Hello world", "email": "jane@doe.com"})
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["location"], "/")