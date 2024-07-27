from sqlalchemy import Column, ForeignKey, Integer, String, cast, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Mapped
from sqlalchemy.dialects.postgresql import JSONB, ARRAY

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
DBSession = sessionmaker(bind=engine)


Base = declarative_base() 

class CastingArray(ARRAY):
    def bind_expression(self, bindvalue):
        return cast(bindvalue, self)
    

class Fleet(Base):
    __tablename__ = 'fleet'
    id = Column(String, primary_key=True)
    filter_conditions = Column(CastingArray(JSONB), nullable=False)

    devices: Mapped[list["DeviceToFleet"]] = relationship()


class Device(Base):
    __tablename__ = 'device'
    id = Column(String, primary_key=True)
    oranisation = Column(String, nullable=True)
    integration = Column(String, nullable=True)
    location_id = Column(String, nullable=True)
    services_enabled = Column(ARRAY(String), nullable=True)
    site_registered_meter_id = Column(String, nullable=True)
    site_id = Column(String, nullable=True)


class DeviceToFleet(Base):
    __tablename__ = 'device_to_fleet'
    device_id = Column(String, ForeignKey('device.id', ondelete="CASCADE"), primary_key=True)
    fleet_id = Column(String, ForeignKey('fleet.id', ondelete="CASCADE"), primary_key=True)
    site_registered_meter_id = Column(String)
    site_id = Column(String, nullable=False)

Base.metadata.create_all(engine)