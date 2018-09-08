from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime, create_engine, Float, ForeignKey, String
from dataclasses import dataclass
from datetime import datetime

Base = declarative_base()


@dataclass
class User(Base):
    __tablename__ = 'user'
    id: int = Column(Integer, primary_key=True)
    last: datetime = Column(DateTime, nullable=False, default=datetime.now())
    period: int = Column(Integer, nullable=False, default=0)
    user_place = relationship("userplace", cascade="all, delete-orphan", backref='order')

    def __init__(self, id):
        self.id = id


@dataclass
class Place(Base):
    __tablename__ = 'place'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    value: float = Column(Float, nullable=False)
    last: datetime = Column(DateTime, nullable=False, default=datetime.now())

    def __init__(self, name, value):
        self.name = name
        self.value = value


@dataclass
class UserPlace(Base):
    __tablename__ = 'userplace'
    user_id: int = Column(Integer, ForeignKey('user.id'), primary_key=True)
    place_id: int = Column(Integer, ForeignKey('place.id'), primary_key=True)


if __name__ == '__main__':
    engine = create_engine('sqlite:///test.db', echo=True)
    Base.metadata.drop_all(engine, checkfirst=True)
    Base.metadata.create_all(engine, checkfirst=True)

    user = User(id=1234)
    place = Place()

    user.id = 2134

    print(user)
