# conn, cursor and DB connection stuff
from spotify import spotify

class artist:
    
    def createArtist(self, artist, genre, no_of_listeners, no_of_albums):
        artist = spotify(artist, genre, no_of_listeners)
        return(artist)

artist1 = artist()

print(artist1.createArtist("The Mystery Van", "indie", 1500, 1))