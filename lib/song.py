class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count(self)
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
      #  self.name = name
       # self.artist = artist
       # self.genre = genre
      #  Song.count += 1

       # self.add_song_to_count()

        #Song.add_to_genres(self)
       # Song.add_to_artists(self)

    @classmethod
    def add_song_to_count(cls, count):
        Song.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        #return genre in cls.genres
  
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        #return artist in cls.artists

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1




        #for genre in genres:
        #    if genre in cls.genre_count:
        #        cls.genre_count[genre] += 1
       # else:
       #     genre_count[genre] = 1
        

        #print({cls.genres : cls.count for genre_count })
        #print({self.name : count for genre in cls.genre_count})

#genre list - keys are the names of each genre
#the COUNT of genre list - value  is the number of songs that have that genre
    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1



#tswift = Song("Karma", "Taylor Swift", "Pop Country")
#print(Song.artists)