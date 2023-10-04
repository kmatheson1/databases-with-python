# Repository Design Recipe Template

_Copy this recipe template to design and implement Model and Repository classes for a database table._


## 1. Design and create the Table

_If the table is already created in the database, you can skip this step._
_Otherwise, follow this recipe to design and create the SQL schema for your table._

|  Record  |             Properties              |
| -------  | ----------------------------------- |
|  recipe  | name, avg_cooking_time_mins, rating |

Name of the table (always plural): `recipes`

Column names: `name`, `avg_cooking_time_mins`, `rating`

## 2. Create Test SQL seeds

_Your tests will depend on data stored in PostgreSQL to run._
_If seed data is provided (or you already created it), you can skip this step._

## 3. Define the class names

_Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name._

'''python
# EXAMPLE
    # Table name: recipes

    # Model class
    # (in lib/recipe.py)
    class Recipe


    # Repository class
    # (in lib/recipe_repository.py)
    class RecipeRepository

'''

## 4. Implement the Model class

_Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys._


'''python
# EXAMPLE
    # Table name: students

    # Model class
    # (in lib/recipe.py)

    class Recipe:
        def __init__(self):
            self.id = 0
            self.title = ""
            self.avg_cooking_time_mins = 0
            self.rating = 0

            # Replace the attributes by your own columns.


    # We can set the attributes to default empty values and set them later,
    # here's an example:
    #
    # >>> recipe = Recipe()
    # >>> recipe.title = "Carbonara"
    # >>> recipe.avg_cooking_time_mins = 30
    # >>> recipe.title
    # 'Carbonara'
    # >>> recipe.avg_cooking_time_mins 
    #  30
'''

## 5. Define the Repository Class interface

_Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database._
_Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method._

'''python
# EXAMPLE
# Table name: recipes

# Repository class
# (in lib/recipe_repository.py)

class RecipeRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, title, avg_cooking_time_mins, rating FROM recipes;

        # Returns an array of Recipe objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, title, avg_cooking_time_mins, rating FROM recipes WHERE id = $1;

        # Returns a single Recipe object.

        # Add more methods below for each operation you'd like to implement.

    # def create(student)
    #

    # def update(student)
    #

    # def delete(student)
    #

'''

## 6. Write Test Examples

_Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5._

'''python
# EXAMPLES

    # 1
    # Get all recipes

    repo = RecipeRepository()

    students = repo.all()

    len(students) # =>  6

    students[0].id # =>  1
    students[0].title # =>  'Carbonara'
    students[0].avg_cooking_time_mins # =>  30
    students[0].rating # =>  4

    students[1].id # =>  2
    students[1].title # =>  'Pizza'
    students[1].avg_cooking_time_mins # =>  60
    students[1].rating # =>  5

    # 2
    # Get a single recipe

    repo = RecipeRepository()

    student = repo.find(1)

    recipe.id # =>  1
    recipe.title # =>  'Carbonara'
    recipe.avg_cooking_time_mins # =>  30
    recipe.rating # =>  4

    # Add more examples for each method

'''

## 7. Test-drive and implement the Repository class behaviour

__After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._