from fastapi import APIRouter, UploadFile, File, HTTPException, status
from fastapi.responses import FileResponse
from pathlib import Path
import uuid
import os

from app.core.config import settings
from app.api.utils import validate_file, remove_background_from_image

router = APIRouter()

@router.post("/remove-background", response_class=FileResponse)
async def remove_background_endpoint(file: UploadFile = File(...)):
    # Validate the file
    validate_file(file)
    
    # Generate unique filenames
    file_ext = file.filename.split(".")[-1]
    input_path = settings.UPLOAD_DIR / f"{uuid.uuid4()}.{file_ext}"
    output_path = settings.UPLOAD_DIR / f"{uuid.uuid4()}_no_bg.png"
    
    try:
        # Save the uploaded file
        with open(input_path, "wb") as buffer:
            buffer.write(await file.read())
        
        # Process the image
        remove_background_from_image(input_path, output_path)
        
        # Return the processed image
        return FileResponse(output_path, media_type="image/png")
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing image: {str(e)}"
        )
    finally:
        # Clean up temporary files if enabled
        if settings.AUTO_CLEANUP:
            if input_path.exists():
                os.remove(input_path)
            if output_path.exists():
                os.remove(output_path)