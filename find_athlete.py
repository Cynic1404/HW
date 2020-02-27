import datetime
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


def find_height(user, session):
    athletes_with_same_height = session.query(Athlete).filter(Athlete.height == user.height)
    if athletes_with_same_height.count() >0:
        first_athlete = athletes_with_same_height.first()
        print(f'Спротсмен с таким же ростом {first_athlete.height} - это {first_athlete.name}')
    else:
        all_athletes = session.query(Athlete)
        list_height = [i.height for i in all_athletes if i.height!=None]
        nearest_height = find_nearest(user.height, list_height)
        athlete_with_nearest_height = session.query(Athlete).filter(Athlete.height == nearest_height).first()
        print(f'Спротсмен, ближайший по росту, это {athlete_with_nearest_height.name}, имеет рост {athlete_with_nearest_height.height}')


def find_birthdate(user, session):
    athletes_with_same_birthdate = session.query(Athlete).filter(Athlete.birthdate == user.birthdate)
    if athletes_with_same_birthdate.count() >0:
        h = session.query(Athlete).filter(Athlete.birthdate == user.birthdate).first()
        print(f'Спротсмен с такой же датой рождения {h.birthdate} - это {h.name}')
    else:
        all_atheletes = session.query(Athlete)
        list_birthdates = [datetime.datetime.strptime(i.birthdate, '%Y-%m-%d') for i in all_atheletes if i.birthdate!=None]
        nearest_birthdate = find_nearest(datetime.datetime.strptime(user.birthdate, '%Y-%m-%d'), list_birthdates)
        athlete_with_nearest_birthdate = session.query(Athlete).filter(Athlete.birthdate == nearest_birthdate.strftime('%Y-%m-%d')).first()
        print(f'Спротсмен, ближайший к дате рождения {user.birthdate}, {athlete_with_nearest_birthdate.name}, был рожден {athlete_with_nearest_birthdate.birthdate}')



def find_nearest(value, list):
    given_value = value
    absolute_difference_function = lambda list_value: abs(list_value - given_value)
    closest_value = min(list, key=absolute_difference_function)
    return closest_value

def main():
    session = connect_db()
    id = input("Введи ID пользователя для поиска: ")
    user = session.query(User).filter(User.id == id)
    if user.count() == 0:
        print('Пользователья с таким id не найдено')
    else:
        find_height(user.first(), session)
        find_birthdate(user.first(), session)


if __name__ == "__main__":
    main()