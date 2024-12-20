import strawberry

@strawberry.type
class UnidadDisponible:
    trip_id: str

@strawberry.type
class Ubicacion:
    shape_pt_lat: float
    shape_pt_lon: float

@strawberry.type
class Alcaldia:
    shape_id: str

@strawberry.type
class Parada:
    stop_name: str
    shape_id: str
