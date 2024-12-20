from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Float, Text, Integer, Date, ForeignKey
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass

class Stop(Base):
    __tablename__ = 'stops'

    stop_id: Mapped[str] = mapped_column(String, primary_key=True)  # Identificador único de la parada
    stop_code: Mapped[str] = mapped_column(String, nullable=True)  # Código opcional de la parada
    stop_name: Mapped[str] = mapped_column(String, nullable=False)  # Nombre de la parada
    stop_desc: Mapped[str] = mapped_column(Text, nullable=True)  # Descripción de la parada (opcional)
    stop_lat: Mapped[float] = mapped_column(Float, nullable=False)  # Latitud de la parada
    stop_lon: Mapped[float] = mapped_column(Float, nullable=False)  # Longitud de la parada
    zone_id: Mapped[str] = mapped_column(String, nullable=True)  # Zona asociada a la parada (opcional)
    stop_url: Mapped[str] = mapped_column(String, nullable=True)  # URL de información adicional (opcional)
    location_type: Mapped[int] = mapped_column(Integer, nullable=True)  # Tipo de ubicación (0: Parada, 1: Estación)
    parent_station: Mapped[str] = mapped_column(String, nullable=True)  # ID de la estación principal (opcional)
    stop_timezone: Mapped[str] = mapped_column(String, nullable=True)  # Zona horaria específica (opcional)
    wheelchair_boarding: Mapped[int] = mapped_column(Integer, nullable=True)  # Accesibilidad para sillas de ruedas
    level_id: Mapped[str] = mapped_column(String, nullable=True)  # ID del nivel donde se encuentra la parada
    platform_code: Mapped[str] = mapped_column(String, nullable=True)  # Código de plataforma (opcional)
    # Relación con StopTime
    stop_times: Mapped[list["StopTime"]] = relationship("StopTime", back_populates="stop")


class Calendar(Base):
    __tablename__ = 'calendar'

    service_id: Mapped[str] = mapped_column(String, primary_key=True)  # Identificador único del servicio
    monday: Mapped[int] = mapped_column(Integer, nullable=False)  # 1 si opera el lunes, 0 si no
    tuesday: Mapped[int] = mapped_column(Integer, nullable=False)  # 1 si opera el martes, 0 si no
    wednesday: Mapped[int] = mapped_column(Integer, nullable=False)  # 1 si opera el miércoles, 0 si no
    thursday: Mapped[int] = mapped_column(Integer, nullable=False)  # 1 si opera el jueves, 0 si no
    friday: Mapped[int] = mapped_column(Integer, nullable=False)  # 1 si opera el viernes, 0 si no
    saturday: Mapped[int] = mapped_column(Integer, nullable=False)  # 1 si opera el sábado, 0 si no
    sunday: Mapped[int] = mapped_column(Integer, nullable=False)  # 1 si opera el domingo, 0 si no
    start_date: Mapped[Date] = mapped_column(Date, nullable=False)  # Fecha de inicio del servicio
    end_date: Mapped[Date] = mapped_column(Date, nullable=False)  # Fecha de fin d


class CalendarDate(Base):
    __tablename__ = 'calendar_dates'

    service_id: Mapped[str] = mapped_column(String, primary_key=True)  # Identificador único del servicio
    date: Mapped[int] = mapped_column(Integer, primary_key=True)  # Fecha de la excepción
    exception_type: Mapped[int] = mapped_column(Integer, nullable=False)


class FeedInfo(Base):
    __tablename__ = 'feed_info'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)  # Clave primaria artificial
    feed_publisher_name: Mapped[str] = mapped_column(String, nullable=False)  # Nombre del publicador del feed
    feed_publisher_url: Mapped[str] = mapped_column(String, nullable=False)  # URL del publicador del feed
    feed_lang: Mapped[str] = mapped_column(String, nullable=False)  # Idioma principal del feed (ISO 639-1)
    default_lang: Mapped[str] = mapped_column(String, nullable=True)  # Idioma por defecto (opcional)
    feed_start_date: Mapped[Date] = mapped_column(Date, nullable=True)  # Fecha de inicio del feed (opcional)
    feed_end_date: Mapped[Date] = mapped_column(Date, nullable=True)  # Fecha de fin del feed (opcional)
    feed_version: Mapped[str] = mapped_column(String, nullable=False)  # Versión del feed
    feed_contact_email: Mapped[str] = mapped_column(String, nullable=True)  # Correo de contacto (opcional)
    feed_contact_url: Mapped[str] = mapped_column(String, nullable=True)  # U



class Shape(Base):
    __tablename__ = 'shapes'

    shape_id: Mapped[str] = mapped_column(String, primary_key=True)  # Identificador único del shape
    shape_pt_lat: Mapped[float] = mapped_column(Float, nullable=False)  # Latitud del punto
    shape_pt_lon: Mapped[float] = mapped_column(Float, nullable=False)  # Longitud del punto
    shape_pt_sequence: Mapped[int] = mapped_column(Integer, primary_key=True)  # Secuencia del punto dentro del shape
    shape_dist_traveled: Mapped[float] = mapped_column(Float, nullable=True)  #

    # Relación con Trip
    trips: Mapped[list["Trip"]] = relationship("Trip", back_populates="shape")



class Routes(Base):
    __tablename__ = 'routes'

    route_id: Mapped[str] = mapped_column(String, primary_key=True)  # Identificador único de la ruta
    agency_id: Mapped[str] = mapped_column(String, nullable=False)  # Identificador de la agencia asociada
    route_short_name: Mapped[str] = mapped_column(String, nullable=False)  # Nombre corto de la ruta
    route_long_name: Mapped[str] = mapped_column(String, nullable=False)  # Nombre largo de la ruta
    route_desc: Mapped[Text] = mapped_column(Text, nullable=True)  # Descripción de la ruta (opcional)
    route_type: Mapped[int] = mapped_column(Integer, nullable=False)  # Tipo de ruta (bus, tren, etc.)
    route_url: Mapped[str] = mapped_column(String, nullable=True)  # URL de la ruta (opcional)
    route_color: Mapped[str] = mapped_column(String(7), nullable=True)  # Color de la ruta (HEX)
    route_text_color: Mapped[str] = mapped_column(String(7), nullable=True)  # Color del texto (HEX)
    route_sort_order: Mapped[int] = mapped_column(Integer, nullable=True)  # Orden de clasificación de la ruta
    continuous_pickup: Mapped[int] = mapped_column(Integer, nullable=True)  # Recogida continua (0: no, 1: sí)
    continuous_drop_off: Mapped[int] = mapped_column(Integer, nullable=True)  # Ba

    # Relación con Agency
    agency: Mapped["Agency"] = relationship("Agency", back_populates="routes")

    # Relación con Trip
    trips: Mapped[list["Trip"]] = relationship("Trip", back_populates="route")



# Modelo StopTime
class StopTime(Base):
    __tablename__ = 'stop_times'

    trip_id: Mapped[str] = mapped_column(String, ForeignKey("trips.trip_id"), primary_key=True)
    stop_id: Mapped[str] = mapped_column(String, ForeignKey("stops.stop_id"), primary_key=True)
    arrival_time: Mapped[str] = mapped_column(String, nullable=False)
    departure_time: Mapped[str] = mapped_column(String, nullable=False)
    stop_sequence: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Relación con Trip
    trip: Mapped["Trip"] = relationship("Trip", back_populates="stop_times")

    # Relación con Stop
    stop: Mapped["Stop"] = relationship("Stop", back_populates="stop_times")

class Trip(Base):
    __tablename__ = 'trips'

    trip_id: Mapped[str] = mapped_column(String, primary_key=True)  # Identificador único del viaje
    route_id: Mapped[str] = mapped_column(String, nullable=False)  # Identificador de la ruta asociada
    service_id: Mapped[str] = mapped_column(String, nullable=False)  # Identificador del servicio asociado
    trip_headsign: Mapped[str] = mapped_column(String, nullable=True)  # Dirección o nombre del destino del viaje
    trip_short_name: Mapped[str] = mapped_column(String, nullable=True)  # Nombre corto del viaje (opcional)
    direction_id: Mapped[int] = mapped_column(Integer, nullable=True)  # Dirección del viaje (0: ida, 1: vuelta)
    block_id: Mapped[str] = mapped_column(String, nullable=True)  # Bloque al que pertenece el viaje (opcional)
    shape_id: Mapped[str] = mapped_column(String, nullable=True)  # Identificador del shape asociado
    wheelchair_accessible: Mapped[int] = mapped_column(Integer, nullable=True)  # Accesibilidad para sillas de ruedas
    bikes_allowed: Mapped[int] = mapped_column(Integer, nullable=True)

    # Relación con Route
    route: Mapped["Routes"] = relationship("Route", back_populates="trips")

    # Relación con StopTime
    stop_times: Mapped[list["Stop"]] = relationship("StopTime", back_populates="trip")

    # Relación con Shape
    shape: Mapped["Shape"] = relationship("Shape", back_populates="trips")



class Agency(Base):
    __tablename__ = 'agency'

    agency_id: Mapped[str] = mapped_column(String, primary_key=True)  # ID único de la agencia
    agency_name: Mapped[str] = mapped_column(String, nullable=False)  # Nombre de la agencia
    agency_url: Mapped[str] = mapped_column(String, nullable=False)  # URL de la agencia
    agency_timezone: Mapped[str] = mapped_column(String, nullable=False)  # Zona horaria de la agencia
    agency_lang: Mapped[str] = mapped_column(String, nullable=True)  # Idioma de la agencia (opcional)
    agency_phone: Mapped[str] = mapped_column(String, nullable=True)  # Teléfono de contacto (opcional)
    agency_fare_url: Mapped[str] = mapped_column(String, nullable=True)  # URL de tarifas (opcional)
    agency_email: Mapped[str] = mapped_column(String, nullable=True)  # Correo de

    routes: Mapped[list["Routes"]] = relationship("Route", back_populates="agency")


