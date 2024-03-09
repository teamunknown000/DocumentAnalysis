from fastapi import APIRouter, File, Form, UploadFile, status
from server.utils.random import random_id
from os import path

router = APIRouter(prefix="/file")


@router.post("/upload")
async def index(
    file: UploadFile = File(...)
):
    file_name = file.filename
    if not file_name:
        file_name = random_id()
    else:
        file_name = random_id()+"."+file_name.split(".").pop()
    content = file.file.read()
    with open(path.join("assets", file_name), "wb") as f:
        f.write(content)
    return {
        "status": 200,
        "file_name": file_name
    }
