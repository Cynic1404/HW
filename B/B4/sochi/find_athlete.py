import uuid

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"

Base = declarative_base()

class Athlete(Base):
    __tablename__ = "athelete"
    id = sa.Column(sa.INTEGER, primary_key=True)
    age = sa.Column(sa.INTEGER)
    birthdate = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    height = sa.Column(sa.INTEGER)
    name = sa.Column(sa.TEXT)
    weight = sa.Column(sa.INTEGER)
    gold_medals = sa.Column(sa.INTEGER)
    silver_medals = sa.Column(sa.INTEGER)
    bronze_medals = sa.Column(sa.INTEGER)
    total_medals = sa.Column(sa.INTEGER)
    sport = sa.Column(sa.TEXT)
    country = sa.Column(sa.TEXT)

class User(Base):
    __tablename__ = "user"
    id = sa.Column(sa.INTEGER, primary_key=True)
    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)


def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def find_height(id, session):
    user = session.query(User).filter(User.id == id)
    if user.count() == 0:
        print('нет таких')
    else:
        athletes_with_same_height = session.query(Athlete).filter(Athlete.height == user.first().height)
        if athletes_with_same_height.count() >0:
            first_athlete = athletes_with_same_height.first()
            print(f'Спротсмен с таким же ростом {first_athlete.height} - это {first_athlete.name}')
        else:
            all_athletes = session.query(Athlete)
            list_height = [i.height for i in all_athletes if i.height!=None]


            given_value = user.first().height
            absolute_difference_function = lambda list_value: abs(list_value - given_value)
            closest_value = min(list_height, key=absolute_difference_function)
            b = session.query(Athlete).filter(Athlete.height == closest_value).first()
            print(f'Спротсмен, ближайший по росту, это {b.name}. Его рост - {b.height}')


def find_birthdate(id, session):
    user = session.query(User).filter(User.id == id)
    if user.count() == 0:
        print('нет таких')
    else:
        if session.query(Athlete).filter(Athlete.birthdate == user.first().birtdate).count() >0:
            h = session.query(Athlete).filter(Athlete.birthdate == user.first().birtdate).first()
            print(f'Спротсмен с таким же ростом {h.height} - это {h.name}')
        else:
            all_atheletes = session.query(Athlete).order_by(Athlete.height.desc())
            list_height = [i.height for i in all_atheletes if i.height!=None]
            given_value = user.first().height
            absolute_difference_function = lambda list_value: abs(list_value - given_value)
            closest_value = min(list_height, key=absolute_difference_function)
            b = session.query(Athlete).filter(Athlete.height == closest_value).first()
            print(f'Спротсмен, ближайший по росту, это {b.name}. Его рост - {b.height}')


def main():
    session = connect_db()
    id = input("Введи ID пользователя для поиска: ")
    find_height(id, session)


if __name__ == "__main__":
    main()