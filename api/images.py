from dotenv import load_dotenv
from imagekitio import ImageKit
import os
from pathlib import Path

# .env dosyasının tam yolunu belirt
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# ImageKit SDK 5.x - sadece private_key kullanılıyor
# IMAGEKIT_PRIVATE_KEY environment variable'dan otomatik okunur
imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
)