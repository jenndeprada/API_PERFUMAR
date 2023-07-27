
from pydantic import BaseModel
from uuid import UUID


class PerfumeModel(BaseModel):
    id:UUID
    name:str
    brand:str
