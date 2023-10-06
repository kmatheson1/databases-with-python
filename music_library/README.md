## Music Library Project 

# Exercise

You have the code for handling the Artist data, now your assignment is to test-drive two new classes; an Album class and an AlbumRepository class with an all method, using the Design Recipe above.

Work in the music_library project you created earlier.

Test-drive an Album class that has attributes for each column in the albums table. You can find the table in seeds/music_library.sql.

Test-drive an AlbumRepository class that has a method all that returns a list of Album objects.

Write a small program in app.py using the class AlbumRepository to print out the list of albums to the terminal.


# Exercise

Your assignment is to:

Test-drive a find method for your AlbumRepository class.

Modify app.py to print to the terminal the album with id 1 using your new find method.

Use your music_library project from the previous section.


# Challenge

Your assignment is to:

Test-drive a create method for your AlbumRepository class.

Test-drive a delete method for your AlbumRepository class.

Use your music_library project from the previous section.


# Exercise

It should work like this:

```bash
; pipenv shell
; python app.py

Welcome to the music library manager!

What would you like to do?
 1 - List all albums
 2 - List all artists

Enter your choice: 1
[ENTER]

Here is the list of albums:
 * 1 - Doolittle
 * 2 - Surfer Rosa
 * 3 - Waterloo
 * 4 - Super Trouper
 * 5 - Bossanova
 * 6 - Lover
 * 7 - Folklore
 * 8 - I Put a Spell on You
 * 9 - Baltimore
 * 10 -	Here Comes the Sun
 * 11 - Fodder on My Wings
 * 12 -	Ring Ring
 ```