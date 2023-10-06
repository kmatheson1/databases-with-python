## Blog 2 Project 

# Exercise

Set up a new project blog for this exercise.

Test-drive and implement Model and Repository classes for the table posts, 
with the method PostRepository#find_by_tag having the behaviour described above.

# Challenge

For this challenge, reuse the database schema created in the previous section (with the Many-to-Many between posts and tags).

Test-drive and implement Model and Repository classes for the table tags, with the method TagRepository#find_by_post. This method should accept a post ID, and return an array of related Tag objects.