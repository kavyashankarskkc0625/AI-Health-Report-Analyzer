import uuid
import os
from datetime import datetime
from fastapi import UploadFile
from database import save_upload, get_uploads_by_user

ALLOWED_TYPES = [
    "application/pdf",
    "image/jpeg",
    "image/png",
    "image/jpg"
]

MAX_FILE_SIZE = 10 * 1024 * 1024

# Folder to save uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Keep metadata in memory
uploaded_files = []


async def upload_file(file: UploadFile, current_user: dict):

    if file.content_type not in ALLOWED_TYPES:
        return {
            "error": "Invalid file type! Only PDF, JPG, PNG allowed!"
        }

    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        return {
            "error": "File too large! Maximum size is 10MB!"
        }

    report_id = str(uuid.uuid4())

    file_key = f"{current_user['email']}/{report_id}/{file.filename}"

    file_size = f"{len(contents)/1024:.2f} KB"

    # Save file physically on server
    filename = f"{report_id}_{file.filename}"
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    with open(filepath, "wb") as f:
        f.write(contents)

    # Save metadata to SQLite
    save_upload(
        report_id,
        file_key,
        file.filename,
        file.content_type,
        file_size,
        current_user["email"],
        current_user["role"]
    )

    # Store metadata in memory
    uploaded_files.append({
        "report_id": report_id,
        "file_key": file_key,
        "file_name": file.filename,
        "file_type": file.content_type,
        "file_size": file_size,
        "uploaded_by": current_user["email"],
        "role": current_user["role"],
        "uploaded_at": datetime.now().isoformat(),
        "filepath": filepath
    })

    return {
        "message": "File uploaded successfully!",
        "report_id": report_id,
        "file_key": file_key,
        "file_name": file.filename,
        "file_type": file.content_type,
        "file_size": file_size,
        "uploaded_by": current_user["email"],
        "uploaded_at": datetime.now().isoformat()
    }


def get_my_uploads(current_user: dict):
    uploads = get_uploads_by_user(current_user["email"])
    return {
        "total": len(uploads),
        "uploads": uploads
    }


def get_file_by_id(report_id: str):
    for f in uploaded_files:
        if f["report_id"] == report_id:
            return f
    return None