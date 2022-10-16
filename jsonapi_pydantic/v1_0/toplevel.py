from typing import List, Optional, Union

from pydantic import BaseModel, Field, conlist, root_validator

from jsonapi_pydantic.v1_0.error import Error
from jsonapi_pydantic.v1_0.jsonapi import JsonApi as JsonApiObject
from jsonapi_pydantic.v1_0.links import Links as LinksObject
from jsonapi_pydantic.v1_0.meta import Meta as MetaObject
from jsonapi_pydantic.v1_0.resource.resource import Resource
from jsonapi_pydantic.v1_0.resource_identifier import ResourceIdentifier

Data = Union[
    None,
    Resource,
    ResourceIdentifier,
    conlist(Resource, min_items=0, unique_items=True),
    conlist(ResourceIdentifier, min_items=0, unique_items=True),
]
Errors = Optional[List[Error]]
Meta = Optional[MetaObject]

JsonApi = Optional[JsonApiObject]
Links = Optional[LinksObject]
Included = Optional[conlist(Resource, min_items=0, unique_items=True)]


class TopLevel(BaseModel):
    data: Data = Field(title="Data")
    errors: Errors = Field(title="Errors")
    meta: Meta = Field(title="Meta")

    jsonapi: JsonApi = Field(title="JSON:API")
    links: Links = Field(title="Links")
    included: Included = Field(title="Included")

    @root_validator
    def check_all_values(cls, values: dict) -> dict:
        # More about these restrictions: https://jsonapi.org/format/#document-top-level
        if values.get("data") and values.get("errors"):
            raise ValueError("The members data and errors MUST NOT coexist in the same document.")
        if values.get("included") and not values.get("data"):
            raise ValueError(
                "If a document does not contain a top-level data key, the included member MUST NOT be present either."
            )
        if not values.get("data") and not values.get("errors") and not values.get("meta"):
            raise ValueError(
                "A document MUST contain at least one of the following top-level members: data, errors, meta."
            )
        return values


__all__ = ["TopLevel"]
