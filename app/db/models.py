from .connection import Base
import uuid
from sqlalchemy import Column, String, Boolean, TIMESTAMP, ForeignKey, func, Text
from sqlalchemy.dialects.postgresql import UUID

class User(Base):
   __tablename__ = "users"
   user_id = Column(UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4()))
   email = Column(String(255), unique=True, nullable=False, index=True)
   password_hash = Column(String(255), nullable=False)
   is_active = Column(Boolean, default=True)
   created_at = Column(TIMESTAMP, server_default=func.now())
   updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
   deleted_at = Column(TIMESTAMP, nullable=True)

class Task(Base):
   __tablename__ = "tasks"
   task_id = Column(UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4()))
   user_id = Column(UUID(as_uuid=False), ForeignKey(User.user_id, ondelete="CASCADE"))
   title = Column(String(100), nullable=False)
   description = Column(Text, nullable=True)
   status = Column(String(20), default="todo")
   created_at = Column(TIMESTAMP, server_default=func.now())
   updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
   deleted_at = Column(TIMESTAMP, nullable=True)
