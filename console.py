import pdb 
from modules.album import Album
from modules.artist import Artist

import repositories.album_repository as album_repository  
import repositories.artist_repository as artist_repository

artists = artist_repository.select_all()

for artist in artists:
    print(artist.__dict__)
