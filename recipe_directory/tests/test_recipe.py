from lib.recipe import Recipe

"""
test recipe constructs with atributes
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Test Recipe", 30, 5)
    assert recipe.id == 1
    assert recipe.title == "Test Recipe"
    assert recipe.avg_cooking_time_mins == 30
    assert recipe.rating == 5

"""
we can compare two identical recipes
and have them be equal
"""
def test_recipes_are_equal():
    recipe1 = Recipe(1, "Test title", 30, 1)
    recipe2 = Recipe(1, "Test title", 30, 1)
    assert recipe1 == recipe2

"""
we can format recipes into string
"""
def test_recipes_format():
    recipe1 = Recipe(1, "Test title", 30, 1)
    assert str(recipe1) == "Recipe(1, Test title, 30, 1)"