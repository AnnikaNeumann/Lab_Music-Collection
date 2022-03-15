import pdb 
from modules.album import Album
from modules.artist import Artist

import repositories.album_repository as album_repository  
import repositories.artist_repository as artist_repository

album = album_repository.select_all()

for album in album:
    print(album.__dict__)

album_repository.delete_all()

album = album_repository.select_all()

for album in album:
    print(album.__dict__)




def select_all():  
    artists = [] 

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists 

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)


