import strawberry
from typing import List

from app.resolvers import (
    get_unidades_disponibles,
    get_ubicaciones_por_unidad,
    get_alcaldias_disponibles,
    get_paradas_por_alcaldia
)
from app.graphql_types import UnidadDisponible, Ubicacion, Alcaldia, Parada

@strawberry.type
class Query:
    @strawberry.field
    def unidades_disponibles(self) -> List[UnidadDisponible]:
        return get_unidades_disponibles()

    @strawberry.field
    def ubicaciones_por_unidad(self, trip_id: str) -> List[Ubicacion]:
        return get_ubicaciones_por_unidad(trip_id)

    @strawberry.field
    def alcaldias_disponibles(self) -> List[Alcaldia]:
        return get_alcaldias_disponibles()

    @strawberry.field
    def paradas_por_alcaldia(self, shape_id: str) -> List[Parada]:
        return get_paradas_por_alcaldia(shape_id)

schema = strawberry.Schema(query=Query)
