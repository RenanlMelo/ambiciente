from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from api.database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True)
    subtitle = Column(String)  # Mantendo apenas o subtitle
    slug = Column(String, index=True, unique=True)
    
    topics = relationship("Topic", back_populates="article", cascade="all, delete-orphan")

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True)
    content = Column(Text)
    article_id = Column(Integer, ForeignKey("articles.id"), unique=True)

    article = relationship("Article", back_populates="topics")
