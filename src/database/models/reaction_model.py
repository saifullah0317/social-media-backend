from database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import User
    from . import Post

class Reaction(db.Model):
    __tablename__ = "reactions"

    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'))
    post_id: Mapped[str] = mapped_column(ForeignKey('posts.id'))

    user: Mapped['User'] = relationship("User", back_populates="reactions")
    post: Mapped['Post'] = relationship("Post", back_populates="reactions")