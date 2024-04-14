from typing import List, Optional, Union

from pydantic.fields import Field
from pydantic.functional_validators import model_validator
from pydantic.main import BaseModel

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
    List[Resource],
    List[ResourceIdentifier],
]
Errors = Optional[List[Error]]
Meta = Optional[MetaObject]

JsonApi = Optional[JsonApiObject]
Links = Optional[LinksObject]
Included = Optional[List[Resource]]


class TopLevel(BaseModel):
    data: Data = Field(None, title="Data")
    errors: Errors = Field(None, title="Errors")
    meta: Meta = Field(None, title="Meta")

    jsonapi: JsonApi = Field(None, title="JSON:API")
    links: Links = Field(None, title="Links")
    included: Included = Field(None, title="Included")

    @model_validator(mode="before")
    def check_all_values(cls, data: dict) -> dict:
        # More about these restrictions: https://jsonapi.org/format/#document-top-level
        if "data" in data and "errors" in data:
            raise ValueError("The members data and errors MUST NOT coexist in the same document.")

        if "included" in data and "data" not in data:
            raise ValueError(
                "If a document does not contain a top-level data key, the included member MUST NOT be present either."
            )

        if "data" not in data and "errors" not in data and "meta" not in data:
            raise ValueError(
                "A document MUST contain at least one of the following top-level members: data, errors, meta."
            )

        if isinstance(data.get("data"), list):
            hashes = {d._hash for d in data["data"]}
            if len(data["data"]) > len(hashes):
                raise ValueError(
                    "A compound document MUST NOT include more than one resource object for each type and id pair."
                )

        return data


__all__ = ["TopLevel"]
