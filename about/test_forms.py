from django.test import TestCase
from .forms import CollaborateForm

class TestCollaborateForm(TestCase):
    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'test',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Collaboration form is not valid.")

    def test_form_is_invalid_wo_name(self):
        """ Test without name"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Name not provided, but collaboration form is still valid")
    
    def test_form_is_invalid_wo_email(self):
        """ Test without email"""
        form = CollaborateForm({
            'name': 'test',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Email not provided, but collaboration form is still valid")

    def test_form_is_invalid_wo_msg(self):
        """ Test without message"""
        form = CollaborateForm({
            'name': 'test',
            'email': 'test@test.com',
            'message': '',
        })
        self.assertFalse(form.is_valid(), msg="Message not provided, but collaboration form is still valid")
