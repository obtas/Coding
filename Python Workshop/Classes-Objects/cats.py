# class cats:
#     name = "lion"
#     weight = 150
#     patterned = False
    
#     def speech(self):
#         return "I am the fiercest of them all!"
    
# cat1 = cats()

# print(cat1.name)
# print(cat1.speech())

class beyonce:
    
    def __init__(self, song, length, album):
        self.song = song
        self.length = length
        self.album = album
        
    def bms(self):
        return "You won't break my soul!"
        
    def __str__(self):
        return f"The song is: {self.song}, the length of the song is: {self.length} and is from the album: {self.album}"
    
    
beyonce1 = beyonce("Halo", 3.22, "I Am")
beyonce2 = beyonce("Crazy in Love", 2.49, "Dangerously in Love")

print(beyonce1.song)
print(beyonce1)

print(getattr(beyonce1, 'song'))
print(hasattr(beyonce2, 'features'))
setattr(beyonce2, 'features', 'JayZ')
print(setattr(beyonce2, 'features', 'JayZ'))
print(getattr(beyonce2, 'features'))
#delattr(beyonce2, 'features')
