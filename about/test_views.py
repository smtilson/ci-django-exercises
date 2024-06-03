from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About

class TestAboutViews(TestCase):

    def setUp(self):

        self.about = About(title="About title", content="About content")
        self.about.save()

    
    def test_collaboration_form_submission(self):
        """Test submitting collaboration request form"""
        form_data = {
            'name': 'test',
            'email': 'test@test.com',
            'message': 'message'}
        response = self.client.post(reverse('about'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Collaboration request submitted. I will get back to "\
              b"you as soon as I can.",
                      response.content)
        
    def test_about_page_with_collaborate_form(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIn(b"About content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)