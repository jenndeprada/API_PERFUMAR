from sqlalchemy import select, and_, insert, update
from abc import ABC
from sqlalchemy.ext.asyncio import AsyncSession
from API_PERFUMAR.api.repository.db_models import PGPerfume
from api.utils.entity_to_model import map_perfume

from api.entities.Perfume import Perfume

class PostgresPerfumeRepository(ABC):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_perfumes(self) -> list[Perfume]:
        stmt = select(PGPerfume)
        results = (await self.session.scalars(stmt)).unique()

        return list(map(map_perfume, results))