from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/blog_posts_comments.sql")

# Retrieve all artists
repository = PostRepository(connection)


post1 = repository.find_with_comments(1)
print(f'\nName: {post1.name} Contents: {post1.contents}')
for comment in post1.comments:
    print(f'{comment.id}: {comment.name} - {comment.contents}')