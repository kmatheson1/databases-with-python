from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
when we call RecipeRepository#all
We get a list of Recipe objects reflecting the seed data
"""

def test_get_all_recipes(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    repo = RecipeRepository(db_connection)

    recipes = repo.all()

    assert recipes == [
        Recipe(1, 'Carbonara', 30, 4),
        Recipe(2, 'Pizza', 60, 5),
        Recipe(3, 'Noodles', 20, 4),
        Recipe(4, 'Baked Beans', 5, 1),
        Recipe(5, 'Salad', 15, 3),
        Recipe(6, 'Sandwich', 5, 3)
    ]

"""
When we call RecipeRepository#find
We get a single rcipe object reflecting the seed data
"""

def test_get_single_recipe(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    repo = RecipeRepository(db_connection)

    recipe = repo.find(1)
    assert recipe == Recipe(1, 'Carbonara', 30, 4)