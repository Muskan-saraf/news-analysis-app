from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from ..database.database import Base

class NewsSummary(Base):
    __tablename__ = "news_summaries"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    summary = Column(Text)
    implications = Column(Text)
    trends = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)