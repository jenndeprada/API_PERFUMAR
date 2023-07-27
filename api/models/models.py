from typing import List, Optional
from pydantic import BaseModel, Field, validator
from uuid import UUID
from datetime import date



class PerfumeModel(BaseModel):
    name:str
    brand:str
