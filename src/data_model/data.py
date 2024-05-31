"""Holds the overall data interface."""
from pydantic import BaseModel
from typing import Set
from .category import Category
from .query import Query


class Data(BaseModel):
    """Dispatcher that handles MtM relationships between tiles and queries."""
    queries: Set[Query] = set()
    categories: Set[Category] = set()

    def add_query(self, query: Query):
        """Append the query updating the references in the category."""
        self.queries.add(query)

        category: Category
        for category in query.categories:
            for found_cat in self.categories:
                if found_cat == category:
                    found_cat.queries.add(query)
                    self.categories |= {found_cat}
                    break
            else:
                category.queries = {query}
                self.categories |= {category}

        self.__class__.model_validate(self)

    @classmethod
    def model_validate(cls, model, **kwargs):
        super(Data, cls).model_validate(model, **kwargs)

        # #TODO: Validate tile identifiers
        # tile_identifiers = set()
        # duplicates = []
        # for

