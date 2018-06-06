# test_bucketlist.py
import unittest
import os
import json
from app import create_app, db

class RecipesTestCase(unittest.TestCase):
    """This class represents the recipes test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.recipe = {'name': 'Herby Pan-Seared Chicken'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_recipe_creation(self):
        """Test API can create a recipe (POST request)"""
        res = self.client().post('/recipes/', data=self.recipe)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Herby Pan-Seared', str(res.data))

    def test_api_can_get_all_recipes(self):
        """Test API can get a recipes (GET request)."""
        res = self.client().post('/recipes/', data=self.recipe)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/recipes/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Herby Pan-Seared', str(res.data))

    def test_api_can_get_recipie_by_id(self):
        """Test API can get a single recipie by using it's id."""
        rv = self.client().post('/recipes/', data=self.recipe)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/recipes/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Herby Pan-Seared', str(result.data))

    def test_recipe_can_be_edited(self):
        """Test API can edit an existing recipe. (PUT request)"""
        rv = self.client().post(
            '/recipes/',
            data={'name': 'Test, Herby Pan-Seared Chicken'})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/recipes/1',
            data={
                "name": "Test recipe, Herby Pan-Seared Chicken "
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/recipes/1')
        self.assertIn('Test recipe', str(results.data))

    def test_recipe_deletion(self):
        """Test API can delete an existing recipe. (DELETE request)."""
        rv = self.client().post(
            '/recipes/',
            data={'name': 'Test, Herby Pan-Seared Chicken'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/recipes/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/recipes/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
