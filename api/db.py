# Async fonksiyonlardan session üretmek için kullanılır
from collections.abc import AsyncGenerator

# UUID üretmek için (benzersiz id)
import uuid
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
# Async SQLAlchemy bileşenleri
# - AsyncSession: async DB işlemleri
# - create_async_engine: async DB bağlantısı
# - async_sessionmaker: session üretici
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

# ORM taban sınıfı ve tablo ilişkileri
from sqlalchemy.orm import DeclarativeBase, relationship
from  datetime import datetime

# 🔹 Veritabanı bağlantı adresi
# aiosqlite → SQLite için async driver
DATABASE_URL = "sqlite+aiosqlite:///./test.db"


class Base(DeclarativeBase):
    pass



# 🔹 ORM MODEL
class Post(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())

# 🔹 Veritabanı motoru (connection)
engine = create_async_engine(DATABASE_URL)

# 🔹 Async session uretıcı
# expire_on_commit=False → commit sonrası nesneler silinmez
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# 🔹 Veritabanı ve tabloları oluşturan fonksiyon
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# 🔹 FastAPI için DB session dependency
# Her request için:
# - session açılır
# - işlem biter
# - session otomatik kapanır
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
