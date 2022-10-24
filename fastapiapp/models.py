from sqlalchemy import String, Column, Text, DateTime

from fastapiapp.db import Base


class Post(Base):
    id = Column(String(50), primary_key=True)

    title = Column(String(200))
    text = Column(Text, nullable=False)

    created = Column(DateTime(timezone=True))