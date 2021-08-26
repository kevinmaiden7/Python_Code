class Singer:

    def __init__(self, name, age): # Constructor method
        self.__name = name
        self.__age = age
        self.__role = "I'm the vocalist of the band"
        self.__lastname = "" # empty string

    # Access Methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_role(self):
        return self.__role

    def get_lastname(self):
        return self.__lastname
    def set_lastname(self, lastname):
        self.__lastname = lastname

    def __str__(self):
        return "Hello, this is " + self.__name + " " + self.__lastname

# End Class Singer

class Album:

    def __init__(self, title):
        self.__title = title
        self.__tracks = [] # empty list
    
    @property
    def title(self):
        return self.__title

    @property
    def tracks(self):
        return self.__tracks

    def add_track(self, new_track):
        self.tracks.append(new_track)
        print("New track added to "+ self.title)
    
    def __str__(self):
        return "Album " + self.title

# End Class Album

class Band:

    # Class Attributes
    BAND_INFO = "Class for storing some metal bands"
    __GENRE = "Metal"

    def __init__(self, name, country, num_members, singer:Singer):
        # Instance Attributes
        self.__name = name
        self.__country = country
        self.__num_members = num_members
        self.__studio_albums = []
        self.__singer = singer # an instance of Singer Class

    @property
    def name(self):
        return self.__name

    @property
    def country(self):
        return self.__country

    @property
    def num_members(self):
        return self.__num_members

    @property
    def studio_albums(self):
        return self.__studio_albums

    def add_album(self, new_album):
        self.studio_albums.append(new_album)
        print("New studio album added for " + self.name)

    @property
    def singer(self):
        return self.__singer

    def __prepare(self, location): # Private function
        print(self.name + " is getting ready for the stage in " + location)

    def go_live(self, location):
        self.__prepare(location)
        print("Now they are playing some " + self.__GENRE)

    @classmethod
    def what_do_we_like(cls): # This is a class method: it can only access Class Attributes
        return "We like " + cls.__GENRE + "!"

    def __str__(self):
        return "We are " + self.name

# End Class Band

# SOME PYTHON CODE
singer_1 = Singer("Bruce", 63)
print(singer_1)
print(singer_1.get_name(), singer_1.get_age())
print(singer_1.get_lastname())
singer_1.set_lastname("Dickinson")
print(singer_1.get_lastname())
print()

album_1 = Album("Powerslave")
print(album_1)
print(album_1.title, album_1.tracks)
tracks = ("Aces High", "The Rime of the Ancient Mariner", "Two Minutes to Midnight", "Flash of the Blade")
for track in tracks:
    album_1.add_track(track)
print(album_1.tracks)

album_2 = Album("Piece of Mind")
tracks = ("The Trooper", "Revelations", "Flight of Icarus", "Where Eagles Dare")
for track in tracks:
    album_2.add_track(track)
print(album_2.tracks)
print()
print(Band.what_do_we_like())
print(Band.BAND_INFO)
print()

maiden = Band("Iron Maiden", "UK", 6, singer_1)
print(maiden)
maiden.go_live("Medellin")
print()

print(maiden.name)
maiden_singer = maiden.singer
print(maiden_singer.get_name())
print(maiden_singer.get_role())

print(maiden.studio_albums)
maiden.add_album(album_1)
maiden.add_album(album_2)
print(maiden.studio_albums)

for album in maiden.studio_albums:
    print(album)
    for track in album.tracks:
        print(track)
    print()
