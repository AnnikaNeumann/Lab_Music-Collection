from db.run_sql import run_sql

from modules.album import Album
from modules.artist import Artist 
# import repositories.artist_repository as a_repository

def select_all():  
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row['title'], row['genre'], row['artist_id'])
        albums.append(album)
    return albums 

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)