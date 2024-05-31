from django.test import TestCase
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Test Category")
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(str(category), "Test Category")

class ImageModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def test_image_creation(self):
        image_content = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')

        image = Image.objects.create(
            title="Test Image",
            image=image_content,
            created_date=date.today(),
            age_limit=18
        )
        image.categories.add(self.category)

        self.assertEqual(image.title, "Test Image")
        self.assertTrue(image.image.name.startswith('images/test_image'))
        self.assertEqual(image.created_date, date.today())
        self.assertEqual(image.age_limit, 18)
        self.assertIn(self.category, image.categories.all())
        self.assertEqual(str(image), "Test Image")