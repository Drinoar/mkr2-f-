from django.test import TestCase
from .models import Category, Recipe


class CategoryModelTest(TestCase):

    def test_create_category(self):
        category = Category.objects.create(name="Desserts")

        self.assertEqual(category.name, "Desserts")
        self.assertEqual(str(category), "Desserts")


