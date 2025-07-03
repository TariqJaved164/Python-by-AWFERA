from fastapi import HTTPException, status
from rembg import remove
from PIL import Image
import io
from app.core.config import settings

def validate_file(file: UploadFile):
    """Validate the uploaded file"""
    if not file.content_type in settings.ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File type not allowed. Allowed types: {', '.join(settings.ALLOWED_FILE_TYPES)}"
        )
    
    # Check file size
    file.file.seek(0, 2)  # Move to end of file
    file_size = file.file.tell()
    file.file.seek(0)  # Move back to start
    
    if file_size > settings.MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File too large. Max size: {settings.MAX_FILE_SIZE/1_000_000}MB"
        )

def remove_background_from_image(input_path: Path, output_path: Path):
    """Process the image to remove background"""
    with open(input_path, "rb") as input_file:
        input_image = input_file.read()
    
    # Remove background
    output_image = remove(input_image)
    
    # Save the result
    with open(output_path, "wb") as output_file:
        output_file.write(output_image)