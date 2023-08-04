from typing import Dict, Optional, Union

from pydantic.fields import Field
from pydantic.functional_validators import model_validator
from pydantic.main import BaseModel
from pydantic.networks import AnyUrl

from jsonapi_pydantic.v1_0.meta import Meta as MetaObject

Href = Optional[AnyUrl]
Meta = Optional[MetaObject]


class Link(BaseModel):
    href: Href = Field(None, title="Href")
    meta: Meta = Field(None, title="Meta")

    @model_validator(mode="before")
    def check_all_values(cls, data: dict) -> dict:
        # More about these restrictions: https://jsonapi.org/format/#document-links
        if len(data) < 1:
            raise ValueError("A link object can contain the following members: href, meta.")
        return data


Links = Dict[str, Union[AnyUrl, Link, None]]

__all__ = ["Link"]
