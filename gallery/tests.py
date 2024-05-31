from django.test import TestCase
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Test Category")
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(str(category), "Test Category")


