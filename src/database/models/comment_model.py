from database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Post

class Comment(db.Model):
    __tablename__ = "comments"

    id: Mapped[str] = mapped_column(primary_key=True)
    post_id: Mapped[str] = mapped_column(ForeignKey('posts.id'))

    post: Mapped['Post'] = relationship("Post", back_populates="comments")