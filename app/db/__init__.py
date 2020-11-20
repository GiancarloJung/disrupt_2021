import os
import sqlalchemy as db

from app.libs.singleton.singleton_meta import SingletonMeta

from sqlalchemy import BigInteger, Column, Date, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship


Base = declarative_base()

class Database(metaclass=SingletonMeta):
    engine = db.create_engine(os.environ['DATABASE_URL'])
    session = None

    def __init__(self):
        self.session = scoped_session(sessionmaker(bind=self.engine))
        self.connection = self.engine.connect()
        Base.metadata.create_all(self.engine)

        print(f'{self}: DB Instance Created')


class BaseModel(Base):
    __abstract__ = True

    id = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), nullable=True)


class DmCastingGroup(BaseModel):
    __tablename__ = 'dm_casting_groups'

    ft_movie_id = Column(Integer, ForeignKey('ft_movies.id'))
    ft_movie = relationship("FtMovie", back_populates="dm_casting_groups")

    dm_castings = relationship("DmCasting", back_populates="dm_casting_groups")


class DmCasting(BaseModel):
    __tablename__ = 'dm_castings'

    kind = Column(String)
    dm_cast_group_id = Column(Integer, ForeignKey('dm_casting_groups.id'))
    dm_cast_group = relationship("DmCastingGroup", back_populates="dm_casting_groups")

    dm_person_id = Column(Integer, ForeignKey('dm_people.id'))
    dm_person = relationship("DmPerson", back_populates="dm_castings")


class DmCountry(BaseModel):
    __tablename__ = 'dm_countries'

    name = Column(String)
    code = Column(String)

    ft_movie_id = Column(Integer, ForeignKey('ft_movies.id'))
    ft_movie = relationship("FtMovie", back_populates="dm_countries")


class DmGenre(BaseModel):
    __tablename__ = 'dm_genres'

    name = Column(String)

    dm_movie_genres = relationship("DmMovieGenre", back_populates="dm_movie_genres")


class DmMovieGenreGroup(BaseModel):
    __tablename__ = 'dm_movie_genre_groups'

    ft_movie_id = Column(Integer, ForeignKey('ft_movies.id'))
    ft_movie = relationship("FtMovie", back_populates="dm_genre_groups")

    dm_movie_genres = relationship("DmMovieGenre", back_populates="dm_movie_genres")


class DmMovieGenre(BaseModel):
    __tablename__ = 'dm_movie_genres'

    dm_genre_id = Column(Integer, ForeignKey('dm_genres.id'))
    dm_genre = relationship("DmGenre", back_populates="dm_genres")

    dm_movie_genre_group_id = Column(Integer, ForeignKey('dm_movie_genre_groups.id'))
    dm_movie_genre_group = relationship("DmMovieGenre", back_populates="dm_movie_genres")


class DmPerson(BaseModel):
    __tablename__ = 'dm_people'

    name = Column(String)
    alias = Column(String)

    dm_castings = relationship("DmCasting", back_populates="dm_castings")


class DmReview(BaseModel):
    __tablename__ = 'dm_reviews'

    content = Column(Text)
    sentiment = Column(String)

    ft_movie_id = Column(Integer, ForeignKey('ft_movies.id'))
    ft_movie = relationship("FtMovie", back_populates="dm_times")


class DmTime(BaseModel):
    __tablename__ = 'dm_times'

    day = Column(Integer)
    month = Column(Integer)
    year = Column(Integer)
    date = Column(Date)

    ft_movie_id = Column(Integer, ForeignKey('ft_movies.id'))
    ft_movie = relationship("FtMovie", back_populates="dm_times")


class DmType(BaseModel):
    __tablename__ = 'dm_types'

    name = Column(String)
    type = Column(String)

    ft_movie_id = Column(Integer, ForeignKey('ft_movies.id'))
    ft_movie = relationship("FtMovie", back_populates="dm_types")


class FtMovie(BaseModel):
    __tablename__ = 'ft_movies'

    title = Column(String)
    description = Column(Text)
    runtime = Column(Float)
    rating = Column(Float)
    metascore = Column(Float)
    revenue = Column(Float)

    dm_casting_group = relationship("DmCastingGroup", uselist=False, back_populates="ft_movies")
    dm_country = relationship("DmCountry", uselist=False, back_populates="ft_movies")
    dm_movie_genre_group = relationship("DmMovieGenreGroup", uselist=False, back_populates="ft_movies")
    dm_time = relationship("DmTime", uselist=False, back_populates="ft_movies")
    dm_type = relationship("DmType", uselist=False, back_populates="ft_movies")

    dm_reviews = relationship("DmReview", uselist=False, back_populates="ft_movies")
