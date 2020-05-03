
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///users.sqlite3"

Base = declarative_base()

class User(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    # задаем название таблицы
    __tablename__ = 'user'
    # идентификатор пользователя, первичный ключ
    id = sa.Column(sa.String(36), primary_key=True)
    # имя пользователя
    first_name = sa.Column(sa.Text)
    # фамилия пользователя
    last_name = sa.Column(sa.Text)
    # адрес электронной почты пользователя
    email = sa.Column(sa.Text)


class LastSeenLog(Base):
    """
    Описывает структуру таблицу log для хранения времени последней активности пользователя
    """
    # задаем название таблицы
    __tablename__ = 'log'

    # идентификатор пользователя, первичный ключ
    id = sa.Column(sa.String(36), primary_key=True)
    # время последней активности пользователя
    timestamp = sa.Column(sa.DATETIME)


# создаем соединение к базе данных
engine = sa.create_engine(DB_PATH)
# создаем фабрику сессию
Sessions = sessionmaker(engine)
# cоздаем сессию
session = Sessions()

# передаем модель Album в метод session.query и вызываем метод all
users = session.query(User).first()

