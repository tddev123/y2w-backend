import os

from fastapi import APIRouter, Form, HTTPException, Query
from fastapi.responses import FileResponse, JSONResponse

from ..services.downloader import download_from_url

router = APIRouter()


@router.post("/download")
async def download(url: str = Form(...), format: str = Form(...)):
    if not url or not format:
        raise HTTPException(status_code=400, detail="No URL or format provided")

    try:
        file_path, title, size, file_type = download_from_url(url, format)
        size_mb = size / (1024 * 1024)  # Convert size to megabytes
        return JSONResponse(
            content={
                "file_path": file_path,
                "title": title,
                "size": size_mb,
                "type": file_type,
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/download-file")
async def download_file(
    file_path: str = Query(..., description="Path of the file to download"),
):
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        file_path,
        filename=os.path.basename(file_path),
        media_type="application/octet-stream",
    )
