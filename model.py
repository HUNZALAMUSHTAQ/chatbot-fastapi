from pydantic import BaseModel
from typing import Union


class Query(BaseModel):
    question: str
