from database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from . import Reaction
    from . import Comment

class Post(db.Model):
    __tablename__ = "posts"

    id: Mapped[str] = mapped_column(primary_key=True)

    reactions: Mapped[List['Reaction']] = relationship("Reaction", back_populates="post")
    comments: Mapped[List['Comment']] = relationship("Comment", back_populates="post")