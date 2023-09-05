from typing import List, Optional, Union

from pydantic.fields import Field
from pydantic.functional_validators import model_validator
from pydantic.main import BaseModel

from jsonapi_pydantic.v1_0.meta import Meta as MetaObject
from jsonapi_pydantic.v1_0.resource.relationship_links import RelationshipLinks
from jsonapi_pydantic.v1_0.resource_identifier import ResourceIdentifier

Links = Optional[RelationshipLinks]
ResourceLinkage = Union[None, ResourceIdentifier, List[ResourceIdentifier]]
Meta = Optional[MetaObject]


class Relationship(BaseModel):
    links: Links = Field(None, title="Links")
    data: ResourceLinkage = Field(None, title="Resource linkage")
    meta: Meta = Field(None, title="Meta")

    @model_validator(mode="before")
    def check_all_values(cls, data: dict) -> dict:
        # More about these restrictions: https://jsonapi.org/format/#document-resource-object-relationships
        if len(data) < 1:
            raise ValueError(
                "A relationship object MUST contain at least one of the following: links, data, meta."
            )
        return data


__all__ = ["Relationship"]
