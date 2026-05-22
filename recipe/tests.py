from django.test import TestCase
from .models import Category, Recipe


class CategoryModelTest(TestCase):

    def test_create_category(self):
        category = Category.objects.create(name="Desserts")

        self.assertEqual(category.name, "Desserts")
        self.assertEqual(str(category), "Desserts")



class RecipeModelTest(TestCase):

    def test_create_recipe(self):
        category = Category.objects.create(name="Soups")

        recipe = Recipe.objects.create(
            title="Borscht",
            description="Traditional soup",
            instructions="Cook vegetables",
            ingredients="Beetroot, potato, carrot",
            category=category
        )

        self.assertEqual(recipe.title, "Borscht")
        self.assertEqual(recipe.category.name, "Soups")
        self.assertEqual(str(recipe), "Borscht")
