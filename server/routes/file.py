from fastapi import APIRouter , UploadFile , File , Form , status
from typing import Annotated
from pathlib import Path

router = APIRouter(prefix="/file")

assets_dir = Path(__file__).parent/"assets"
assets_dir.mkdir(parents=True, exist_ok=True)

@router.post("/upload")
async def index(
    file: UploadFile = File(...)
):
    return{
        "status":200
    }
    
    
