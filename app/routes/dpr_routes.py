from fastapi import APIRouter, UploadFile
from app.services.dpr_service import process_dpr

router = APIRouter()

@router.post("/upload")
async def upload_dpr(file: UploadFile):
    result = await process_dpr(file)
    return result
