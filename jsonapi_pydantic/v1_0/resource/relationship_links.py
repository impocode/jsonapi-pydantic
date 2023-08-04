from typing import Union

from pydantic.fields import Field
from pydantic.functional_validators import model_validator
from pydantic.main import BaseModel
from pydantic.networks import AnyUrl

from jsonapi_pydantic.v1_0.links import Link

RelationshipLink = Union[AnyUrl, Link, None]
RelatedResourceLink = Union[AnyUrl, Link, None]


class RelationshipLinks(BaseModel):
    self: RelationshipLink = Field(None, title="Relationship link")
    related: RelatedResourceLink = Field(None, title="Related resource link")

    @model_validator(mode="before")
    def check_all_values(cls, data: dict) -> dict:
        # More about these restrictions: https://jsonapi.org/format/#document-resource-object-relationships
        if len(data) < 1:
            raise ValueError(
                "A links object for a relationship that contains at least one of the following: self, related."
            )
        return data


__all__ = ["RelationshipLinks"]
