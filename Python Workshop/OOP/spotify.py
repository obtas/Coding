class spotify:
    def __init__(self, artist, genre, no_of_listeners):
        self.artist = artist
        self.genre = genre
        self.no_of_listeners = no_of_listeners
        
    def listen(self):
        return "listen to me on spotify!"
    
    def __str__(self):
        return f"artist = {self.artist}"