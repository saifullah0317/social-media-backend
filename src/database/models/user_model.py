from database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from . import Content
    from . import Reaction

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    profile_pic: Mapped[str] = mapped_column(nullable=True)

    contents: Mapped[List['Content']] = relationship("Content", back_populates="user")
    reactions: Mapped[List['Reaction']] = relationship("Reaction", back_populates="user")