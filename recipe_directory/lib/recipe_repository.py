from lib.recipe import Recipe

class RecipeRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        recipes = []

        for row in rows:
            item = Recipe(row["id"], row["title"], row["avg_cooking_time_mins"], row["rating"])
            recipes.append(item)
        return recipes

    def find(self, id):
        rows = self._connection.execute('SELECT * from recipes WHERE id = %s', [id])
        row = rows[0]
        return Recipe(row["id"], row["title"], row["avg_cooking_time_mins"], row["rating"])
