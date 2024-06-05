from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Constellation(Base):
    __tablename__ = 'constellations'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class Star(Base):
    __tablename__ = 'stars'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    x_coord = Column(Integer)
    y_coord = Column(Integer)
    description = Column(String)
    constellation_id = Column(Integer, ForeignKey('constellations.id'))
    constellation = relationship('Constellation', backref='stars')
    size = Column(String)  # big, small, medium

engine = create_engine('sqlite:///stars.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

constellations = [
    {'name': 'Orion', 'description': 'Hunter constellation'},
    {'name': 'Cassiopeia', 'description': 'Queen constellation'},
    {'name': 'Ursa Major', 'description': 'Great Bear constellation'},
    {'name': 'Ursa Minor', 'description': 'Little Bear constellation'},
    {'name': 'Draco', 'description': 'Dragon constellation'},
    {'name': 'Bootes', 'description': 'Herdsman constellation'},
    {'name': 'Virgo', 'description': 'Maiden constellation'},
    {'name': 'Libra', 'description': 'Scales constellation'},
    {'name': 'Scorpius', 'description': 'Scorpion constellation'},
    {'name': 'Sagittarius', 'description': 'Archer constellation'},
    {'name': 'Capricornus', 'description': 'Sea-goat constellation'},
    {'name': 'Aquarius', 'description': 'Water bearer constellation'},
    {'name': 'Pisces', 'description': 'Fish constellation'},
    {'name': 'Aries', 'description': 'Ram constellation'},
    {'name': 'Taurus', 'description': 'Bull constellation'},
    {'name': 'Gemini', 'description': 'Twins constellation'},
    {'name': 'Cancer', 'description': 'Crab constellation'},
    {'name': 'Leo', 'description': 'Lion constellation'},
    {'name': 'Virgo', 'description': 'Maiden constellation'},
    {'name': 'Libra', 'description': 'Scales constellation'},
]

for constellation in constellations:
    session.add(Constellation(**constellation))
session.commit()

# Insert stars
stars = [
    {'name': 'Sirius', 'x_coord': 100, 'y_coord': 200, 'description': 'Brightest star in the night sky', 'size': 'большой', 'constellation_id': 1},
    {'name': 'Canopus', 'x_coord': 50, 'y_coord': 150, 'description': 'Second-brightest star in the night sky', 'size': 'большой', 'constellation_id': 2},
    {'name': 'Arcturus', 'x_coord': 200, 'y_coord': 300, 'description': 'Orange giant star', 'size': 'средний', 'constellation_id': 3},
    {'name': 'Vega', 'x_coord': 150, 'y_coord': 250, 'description': 'Bright white star', 'size': 'маленький', 'constellation_id': 4},
    {'name': 'Capella', 'x_coord': 250, 'y_coord': 350, 'description': 'Yellow-orange giant star', 'size': 'средний', 'constellation_id': 5},
    {'name': 'Aldebaran', 'x_coord': 300, 'y_coord': 400, 'description': 'Orange giant star', 'size': 'большой', 'constellation_id': 6},
    {'name': 'Spica', 'x_coord': 350, 'y_coord': 450, 'description': 'Blue-white star', 'size': 'маленький', 'constellation_id': 7},
    {'name': 'Antares', 'x_coord': 400, 'y_coord': 500, 'description': 'Red supergiant star', 'size': 'большой', 'constellation_id': 8},
    {'name': 'Acrux', 'x_coord': 450, 'y_coord': 550, 'description': 'Blue-white star', 'size': 'маленький', 'constellation_id': 9},
    {'name': 'Gacrux', 'x_coord': 500, 'y_coord': 600, 'description': 'Red giant star', 'size': 'средний', 'constellation_id': 10},
    {'name': 'Rigel', 'x_coord': 550, 'y_coord': 650, 'description': 'Blue-white star', 'size': 'большой', 'constellation_id': 11},
    {'name': 'Procyon', 'x_coord': 600, 'y_coord': 700, 'description': 'Yellow-white star', 'size': 'средний', 'constellation_id': 12},
    {'name': 'Betelgeuse', 'x_coord': 650, 'y_coord': 750, 'description': 'Red supergiant star', 'size': 'большой', 'constellation_id': 13},
    {'name': 'Deneb', 'x_coord': 700, 'y_coord': 800, 'description': 'Blue-white star', 'size': 'маленький', 'constellation_id': 14},
    {'name': 'Altair', 'x_coord': 750, 'y_coord': 850, 'description': 'Yellow-white star', 'size': 'средний', 'constellation_id': 15},
    {'name': 'Vega', 'x_coord': 800, 'y_coord': 900, 'description': 'Bright white star', 'size': 'маленький', 'constellation_id': 16},
    {'name': 'Capella', 'x_coord': 850, 'y_coord': 950, 'description': 'Yellow-orange giant star', 'size': 'средний', 'constellation_id': 17},
    {'name': 'Aldebaran', 'x_coord': 900, 'y_coord': 1000, 'description': 'Orange giant star', 'size': 'большой', 'constellation_id': 18},
    {'name': 'Spica', 'x_coord': 950, 'y_coord': 1050, 'description': 'Blue-white star', 'size': 'маленький', 'constellation_id': 19},
    {'name': 'Antares', 'x_coord': 1000, 'y_coord': 1100, 'description': 'Red supergiant star', 'size': 'большой', 'constellation_id': 20},
]

for star in stars:
    session.add(Star(**star))
session.commit()

def get_all_stars():
    return session.query(Star).all()

def get_all_constellations():
    return session.query(Constellation).all()

def get_star_by_id(star_id):
    return session.query(Star).get(star_id)

def get_constellation_by_id(constellation_id):
    return session.query(Constellation).get(constellation_id)