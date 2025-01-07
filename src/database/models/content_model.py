from database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ENUM
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import User

class Content(db.Model):
    __tablename__ = "contents"

    id: Mapped[str] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'))
    mediable_type: Mapped[str] = mapped_column(ENUM('post', 'comment', name='mediable_types'), nullable=False)
    mediable_id: Mapped[str] = mapped_column(nullable=False)

    user: Mapped['User'] = relationship("User", back_populates="contents")