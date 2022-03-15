from db.run_sql import run_sql

from modules.album import Album
from modules.artist import Artist 
# import repositories.album_repository as album_repository

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