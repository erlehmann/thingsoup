from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey
from sqlalchemy.orm import relation

from uuid import uuid4

from meta import Base, metadata

from dcmi import DCMI_point

# association table for spatials
things_spatials = Table('things_spatials', metadata,
    Column('thing_uuid', Integer, ForeignKey('things.uuid')),
    Column('spatial_id', Integer, ForeignKey('dcterms_spatials.id'))
)

class Thing(Base):
        __tablename__ = 'things'
        
        uuid = Column(String(36), primary_key=True)
        # str(uuid.uuid4()).__len__() is always 36

        dc_title = Column(String)
        dc_description = Column(String)
        dc_type = Column(String)

        # many to many relationship for spatials
        dcterms_spatials = relation('DCMI_point', secondary='things_spatials', backref='things')

        def __init__(self, title, description='', type='PhysicalObject'):
            self.uuid = str(uuid4())

            self.dc_title = title
            self.dc_description = description
            self.dc_type = type

        def __repr__(self):
            return "<Thing(id=%d, thing=%s)>" % (self.uuid, self.title)
