
from api.repository.db_models import PGPerfume
from api.entities.Perfume import Perfume


def map_perfume(perfume:PGPerfume) -> Perfume:
    return Perfume(
        id = perfume.id,
        name = perfume.name,
        brand = perfume.brand
    )