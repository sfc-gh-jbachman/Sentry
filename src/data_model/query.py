from pydantic import BaseModel
from typing import Set, ForwardRef


class Query(BaseModel):
    categories: Set[ForwardRef("Category")] = set()
    text: str

    __hash__ = object.__hash__
