from pathlib import Path

class Settings:
    PROJECT_NAME: str = "Background Remover API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "API to remove backgrounds from images using AI"
    
    # File upload settings
    UPLOAD_DIR: Path = Path("uploads")
    MAX_FILE_SIZE: int = 8_000_000  # 8MB
    ALLOWED_FILE_TYPES: list = ["image/jpeg", "image/png", "image/webp"]
    
    # Cleanup settings
    AUTO_CLEANUP: bool = True
    
    class Config:
        case_sensitive = True

settings = Settings()