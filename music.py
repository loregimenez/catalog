from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Genre, Base, Song, User

engine = create_engine('sqlite:///music.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# create a dummy user
User1 = User(name="user1", email="user1@music.com",
             picture='http://i64.tinypic.com/j80409.png')
session.add(User1)
session.commit()

User2 = User(name="user2", email="user2@music.com",
             picture='http://i64.tinypic.com/5v51i.png')
session.add(User2)
session.commit()

User3 = User(name="user3", email="user3@music.com",
             picture='http://i63.tinypic.com/2dcfjuf.png')
session.add(User3)
session.commit()

# Pop Genre
popGenre = Genre(name = "Pop", user_id = 1)

session.add(popGenre)
session.commit()

song1 = Song(name = "Havana",
			band_name = "Camila Cabello",
			country = "US",
			youtube_url = "https://youtu.be/HCjNJDNzw8Y",
			genre = popGenre,
            user_id = 1)
session.add(song1)
session.commit()

song2 = Song(name = "Something Just Like This",
			band_name = "The Chainsmokers & Coldplay",
			country = "US",
			youtube_url = "https://youtu.be/FM7MFYoylVs",
			genre = popGenre,
            user_id = 1)
session.add(song2)
session.commit()

song3 = Song(name = "Meant to Be",
			band_name = "Bebe Rexha",
			country = "US",
			youtube_url = "https://youtu.be/j5YSOabmFgw",
			genre = popGenre,
            user_id = 1)
session.add(song3)
session.commit()

song4 = Song(name = "Need Somebody",
			band_name = "XUITCASECITY",
			country = "US",
			youtube_url = "https://youtu.be/YmXJp2DNMwk",
			genre = popGenre,
            user_id = 1)
session.add(song4)
session.commit()


# Indie Genre
indieGenre = Genre(name = "Indie", user_id = 1)

song1 = Song(name = "Love Is Mystical",
			band_name = "Cold War Kids",
			country = "US",
			youtube_url = "https://youtu.be/Qbe3oSfUG00",
			genre = indieGenre)
session.add(song1)
session.commit()

song2 = Song(name = "Dig Down",
			band_name = "Muse",
			country = "US",
			youtube_url = "https://youtu.be/b4ozdiGys5g",
			genre = indieGenre)
session.add(song2)
session.commit()

song3 = Song(name = "Creature Comfort",
			band_name = "Arcade Fire",
			country = "US",
			youtube_url = "https://youtu.be/xzwicesJQ7E",
			genre = indieGenre)
session.add(song3)
session.commit()

song4 = Song(name = "Bad Boy",
			band_name = "Dan Croll",
			country = "US",
			youtube_url = "https://youtu.be/J5THiYqJtIA",
			genre = indieGenre)
session.add(song4)
session.commit()

# Rock Genre
rockGenre = Genre(name = "Rock", user_id = 1)

song1 = Song(name = "The Sky Is A Neighborhood",
			band_name = "Foo Fighters",
			country = "US",
			youtube_url = "https://youtu.be/TRqiFPpw2fY",
			genre = rockGenre)
session.add(song1)
session.commit()

song2 = Song(name = "Bad Moon",
			band_name = "Hollywood Undead",
			country = "US",
			youtube_url = "https://youtu.be/sZSdRVkplWQ",
			genre = rockGenre)
session.add(song2)
session.commit()

song3 = Song(name = "How Did We Get So Dark?",
			band_name = "Royal Blood",
			country = "US",
			youtube_url = "https://youtu.be/sbx95gBb5HM",
			genre = rockGenre,
            user_id = 1)
session.add(song3)
session.commit()

song4 = Song(name = "The Resistance",
			band_name = "Skillet",
			country = "US",
			youtube_url = "https://youtu.be/SKnRdQiH3-k",
			genre = rockGenre,
            user_id = 1)
session.add(song4)
session.commit()
