from typing import Optional, Union

from pydantic import BaseModel, Field, conlist, root_validator

from jsonapi_pydantic.v1_0.meta import Meta as MetaObject
from jsonapi_pydantic.v1_0.resource.relationship_links import RelationshipLinks
from jsonapi_pydantic.v1_0.resource_identifier import ResourceIdentifier

Links = Optional[RelationshipLinks]
ResourceLinkage = Union[
    None, ResourceIdentifier, conlist(ResourceIdentifier, min_items=0, unique_items=True)
]
Meta = Optional[MetaObject]


class Relationship(BaseModel):
    links: Links = Field(title="Links")
    data: ResourceLinkage = Field(title="Resource linkage")
    meta: Meta = Field(title="Meta")

    @root_validator
    def check_all_values(cls, values: dict) -> dict:
        # More about these restrictions: https://jsonapi.org/format/#document-resource-object-relationships
        if len(values) < 1:
            raise ValueError(
                "A relationship object MUST contain at least one of the following: links, data, meta."
            )
        return values


__all__ = ["Relationship"]
