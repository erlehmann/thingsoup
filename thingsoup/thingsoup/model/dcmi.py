from sqlalchemy import Column, Integer, String, Float

from meta import Base

class DCMI_point(Base):
        __tablename__ = 'dcterms_spatials'

        id = Column(Integer, primary_key=True)

        # properties according to http://dublincore.org/documents/dcmi-point/
        east = Column(Float)
        north = Column(Float)
        elevation = Column(Float)
        # units is always signed decimal degrees
        # zunits is always meters
        # projection is always geographic coordinates on Earth for north, east; height above mean-sea-level for elevation.
        name = Column(String)

        def __init__(self, east, north, elevation='0', name=''):
            self.east = east
            self.north = north
            self.elevation = elevation
            self.name = name

        def __repr__(self):
            return "<DCMI point(%f N, %f E, %s)>" % (self.id, self.title)
