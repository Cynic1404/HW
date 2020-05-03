import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///b4_7.sqlite3"

Base = declarative_base()

class Album(Base):
    """
    Описывает структуру таблицы album для хранения записей музыкальной библиотеки
    """
    # указываем имя таблицы
    __tablename__ = "album"
    # Задаем колонки в формате
    # название_колонки = sa.Column(ТИП_КОЛОНКИ)
    # идентификатор строки
    id = sa.Column(sa.INTEGER, primary_key=True)
    # Год записи альбома
    year = sa.Column(sa.INTEGER)
    # артист или группа, записавшие альбом
    artist = sa.Column(sa.TEXT)
    # жанр альбома
    genre = sa.Column(sa.TEXT)
    # название альбома
    album = sa.Column(sa.TEXT)

# создаем соединение к базе данных
engine = sa.create_engine(DB_PATH)
# создаем фабрику сессию
Sessions = sessionmaker(engine)
# создаем сессию
session = Sessions()


heaven_and_earth = session.query(Album).filter(Album.album == "Heaven and Earth").first()
heaven_and_earth.year = 2017
last_ship = Album(year=2013, artist="Sting", genre="Rock", album="The Last Ship")
magic = Album(year=2016, artist="Bruno Mars", genre="Rhythm and blues", album="24K Magic")
session.add_all([heaven_and_earth, last_ship, magic])
session.commit()
# print(heaven_and_earth)
