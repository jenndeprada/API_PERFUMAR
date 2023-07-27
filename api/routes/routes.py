from uuid import UUID
from fastapi import APIRouter
from api.models.models import PerfumeModel
from api.entities.Perfume import Perfume

router = APIRouter()



@router.get("/perfumes", response_model=list[PerfumeModel]) #Modelo de Pydantic
async def list_perfumes() -> list[Perfume]:
    return {
        "name":'perfume_name',
        "brand":'perfume_brand'
    }


@router.get("/perfumes/{id}", response_model=PerfumeModel)
async def get_perfume(id:UUID) -> Perfume:
    pass


