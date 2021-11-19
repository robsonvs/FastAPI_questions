from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Filter(BaseModel):
    name: str
    filter: list
    order: int
    created: Optional[datetime] = None
    updated: Optional[datetime] = None


class Question(BaseModel):

    question: str
    answer: list
    question_filter: str
    #question_filter: Optional[Filter] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None