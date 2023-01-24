class spotify:
    def __init__(self, artist, genre, no_of_listeners):
        self.artist = artist
        self.genre = genre
        self.no_of_listeners = no_of_listeners
        
    def listen(self):
        return "listen to me on spotify!"
    
class beyonce(spotify):
    def __init__(self, artist, genre, no_of_listeners, no_of_albums):
        super().__init__(artist, genre, no_of_listeners)
        self.no_of_albums = no_of_albums
        
    def __str__(self):
        return f"artist: {self.artist}, genre: {self.genre}, number of listeners: {self.no_of_listeners} and number of albums: {self.no_of_albums}"
    
class nct(spotify):
    def __init__(self, artist, genre, no_of_listeners, subunit):
        super().__init__(artist, genre, no_of_listeners)
        self.subunit = subunit
        
    def __str__(self):
        return f"artist: {self.artist}, genre: {self.genre}, number of listeners: {self.no_of_listeners} and subunit: {self.subunit}"
     
beyonce1 = beyonce("Beyonce", "any", 50000000, 6)
nct1 = nct("nct127", "KPop", 2000000, "nct127")
nct2 = nct("nctdream", "KPop", 1750000, "nctdream")
nct3 = nct("wayv", "KPop", 1500000, "wayv")

print(beyonce1)
print(nct1)
print(nct2)
print(nct3)

artists = [beyonce1, nct1, nct2, nct3]

print(artists)

for artist in artists:
    print(artist)
    print(artist.listen())
