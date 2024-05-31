"""Category effectively a collection of queries + metadata."""
from typing import Set, ForwardRef
from pydantic import BaseModel


class Category(BaseModel):
    queries: Set[ForwardRef("Query")] = set()
    name: str

    def __hash__(self):
        return hash(self.name)
