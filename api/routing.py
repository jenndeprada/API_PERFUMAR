from fastapi import APIRouter
from api.routes.routes import router as perfume_router

router = APIRouter()
router.include_router(perfume_router)