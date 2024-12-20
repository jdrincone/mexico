from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database import engine
from app.graphql_types import UnidadDisponible, Ubicacion, Alcaldia, Parada

def get_unidades_disponibles() -> List[UnidadDisponible]:
    with Session(engine) as session:
        result = session.execute(text("SELECT DISTINCT trip_id FROM trips")).mappings().all()
        return [UnidadDisponible(trip_id=row["trip_id"]) for row in result]

def get_ubicaciones_por_unidad(trip_id: str) -> List[Ubicacion]:
    with Session(engine) as session:
        query = text("""
        SELECT shape_pt_lat, shape_pt_lon
        FROM trips t
        LEFT JOIN shapes s ON s.shape_id = t.shape_id
        WHERE t.trip_id = :trip_id
        """)
        result = session.execute(query, {"trip_id": trip_id}).mappings().all()
        return [
            Ubicacion(shape_pt_lat=row["shape_pt_lat"], shape_pt_lon=row["shape_pt_lon"])
            for row in result
        ]

def get_alcaldias_disponibles() -> List[Alcaldia]:
    with Session(engine) as session:
        query = text("SELECT DISTINCT shape_id FROM trips")
        result = session.execute(query).mappings().all()
        return [Alcaldia(shape_id=row["shape_id"]) for row in result]

def get_paradas_por_alcaldia(shape_id: str) -> List[Parada]:
    with Session(engine) as session:
        query = text("""
        SELECT s.stop_name, sh.shape_id
        FROM stops s
        LEFT JOIN shapes sh 
        ON (sh.shape_pt_lat = s.stop_lat AND sh.shape_pt_lon = s.stop_lon)
        WHERE sh.shape_id = :shape_id
        """)
        result = session.execute(query, {"shape_id": shape_id}).mappings().all()
        return [
            Parada(stop_name=row["stop_name"], shape_id=row["shape_id"])
            for row in result
        ]
