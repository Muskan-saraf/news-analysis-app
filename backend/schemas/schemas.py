from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NewsSummaryBase(BaseModel):
    summary: str
    implications: str
    trends: str

class NewsSummaryCreate(NewsSummaryBase):
    pass

class NewsSummary(NewsSummaryBase):
    id: int
    date: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True