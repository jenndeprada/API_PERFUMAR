from uuid import UUID
from fastapi import APIRouter
from api.models.models import PerfumeModel
from api.entities.Perfume import Perfume
from usecases.usecases import get_perfumes
router = APIRouter()



@router.get("/perfumes", response_model=list[PerfumeModel]) #Modelo de Pydantic
async def list_perfumes() -> list[Perfume]:
    list_of_perfumes = await get_perfumes()
    return list_of_perfumes if list_of_perfumes else []


@router.get("/perfumes/{id}", response_model=PerfumeModel)
async def get_perfume(id:UUID) -> Perfume:
    perfume = await get_perfume(id=id)
    return perfume if perfume else None


