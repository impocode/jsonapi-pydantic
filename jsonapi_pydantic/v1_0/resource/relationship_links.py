from typing import Union

from pydantic import AnyUrl, BaseModel, Field, root_validator

from jsonapi_pydantic.v1_0.links import Link

RelationshipLink = Union[AnyUrl, Link, None]
RelatedResourceLink = Union[AnyUrl, Link, None]


class RelationshipLinks(BaseModel):
    self: RelationshipLink = Field(title="Relationship link")
    related: RelatedResourceLink = Field(title="Related resource link")

    @root_validator
    def check_all_values(cls, values: dict) -> dict:
        # More about these restrictions: https://jsonapi.org/format/#document-resource-object-relationships
        if len(values) < 1:
            raise ValueError(
                "A links object for a relationship that contains at least one of the following: self, related."
            )
        return values


__all__ = ["RelationshipLinks"]
