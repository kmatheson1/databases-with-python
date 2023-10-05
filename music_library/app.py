from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):

        while True:
            print('\nWelcome to the music library manager!')
            print('\nWhat would you like to do?')
            print('  1 - List all albums')
            print('  2 - List all artists')

            choice = input('\nEnter your choice: ')

            if choice == '1':
                album_repo = AlbumRepository(self._connection)
                print('\nHere is the list of albums:')
                for album in album_repo.all():
                    print(f'{album.id} - {album.title}')
                
            
            if choice == '2':
                artist_repo = ArtistRepository(self._connection)
                print('\nHere is the list of artists:')
                for artist in artist_repo.all():
                    print(f'{artist.id} - {artist.name}')
            
            break

if __name__ == '__main__':
    app = Application()
    app.run()