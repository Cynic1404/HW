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
    #находим всех атлетов с таким же ростом, как у введенного юзера
    athletes_with_same_height = session.query(Athlete).filter(Athlete.height == user.height)
    #если таких несколько, выводим первого
    if athletes_with_same_height.count() >0:
        first_athlete = athletes_with_same_height.first()
        print(f'Спротсмен с таким же ростом {first_athlete.height} - это {first_athlete.name}')
    # если атлетов с таким же ростом, как у введенного юзера, нет, находим ближайшего
    else:
        #находим всех атлетов
        all_athletes = session.query(Athlete)
        #составляем список с ростом всех спростменов
        list_height = [i.height for i in all_athletes if i.height!=None]
        #находим ближайший рост к росту введенного юзера
        nearest_height = find_nearest(user.height, list_height)
        #находим спротсмена с ближайшим ростом
        athlete_with_nearest_height = session.query(Athlete).filter(Athlete.height == nearest_height).first()
        #распесатываем информацию о нем
        print(f'Спротсмен, с ростом, ближайшим к {user.height}, это {athlete_with_nearest_height.name}, имеет рост {athlete_with_nearest_height.height}')


def find_birthdate(user, session):
    # находим всех атлетов с такой же датой рождения, как у введенного юзера
    athletes_with_same_birthdate = session.query(Athlete).filter(Athlete.birthdate == user.birthdate)
    # если таких несколько, выводим первого
    if athletes_with_same_birthdate.count() >0:
        h = session.query(Athlete).filter(Athlete.birthdate == user.birthdate).first()
        print(f'Спротсмен с такой же датой рождения {h.birthdate} - это {h.name}')
    # если атлетов с такой же датой рождения, как у введенного юзера, нет, находим ближайшего
    else:
        # находим всех атлетов
        all_atheletes = session.query(Athlete)
        # составляем список с ДР всех спростменов
        list_birthdates = [datetime.datetime.strptime(i.birthdate, '%Y-%m-%d') for i in all_atheletes if i.birthdate!=None]
        # находим ближайший ДР к росту введенного юзера
        nearest_birthdate = find_nearest(datetime.datetime.strptime(user.birthdate, '%Y-%m-%d'), list_birthdates)
        # находим спротсмена с ближайшим ДР
        athlete_with_nearest_birthdate = session.query(Athlete).filter(Athlete.birthdate == nearest_birthdate.strftime('%Y-%m-%d')).first()
        # распесатываем информацию о нем
        print(f'Спротсмен с датой рождения, ближайшей к {user.birthdate}, это {athlete_with_nearest_birthdate.name}, был рожден {athlete_with_nearest_birthdate.birthdate}')


"""
данная функция находит в листе list ближайшее значение к value
Не стоит вникать, как это работает =)
"""
def find_nearest(value, list):
    given_value = value
    absolute_difference_function = lambda list_value: abs(list_value - given_value)
    closest_value = min(list, key=absolute_difference_function)
    return closest_value



def main():
    '''
    изначально проверяется, есть ли в базе пользователь с таким id
    Если такого пользователья нет, то печататся соответсвующее сообщени
    Если пользоваткль есть, то мы начинвем искать в другой таблице спростоменов
    с такими же/ближайшими ростом и датой рождения
    '''
    session = connect_db()
    id = input("Введи ID пользователя для поиска: ")
    user = session.query(User).filter(User.id == id)
    if user.count() == 0:
        print('Пользователя с таким id не найдено')
    else:
        find_height(user.first(), session)
        find_birthdate(user.first(), session)


if __name__ == "__main__":
    main()