import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"

Base = declarative_base()

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
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()


def request_data():
    print("Привет! Я запишу твои данные!")
    first_name = input("Введи своё имя: ")
    last_name = input("А теперь фамилию: ")
    email = input("Мне еще понадобится адрес твоей электронной почты: ")
    gender = input("Пол: ")
    birthdate = input("Дата рождения: ")
    height = 0
    while int(height) <= 120  or  int(height) >= 300:
        print('Веедите рост в см (120-300)')
        height = input("Рост: ")
    height = height[0]+'.'+height[1:]
    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        gender = gender,
        birthdate = birthdate,
        height = height
    )
    return user

def find(id, session):
    if session.query(User).filter(User.id == id).count() == 0:
        print('нет таких')
    else:
        user = session.query(User).filter(User.id == id)
        for i in user:
            print(i.first_name)


def main():
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Спасибо, данные сохранены!")



if __name__ == "__main__":
    main()