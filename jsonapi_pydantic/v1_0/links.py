from typing import Dict, Optional, Union

from pydantic import AnyUrl, BaseModel, Field, root_validator

from jsonapi_pydantic.v1_0.meta import Meta as MetaObject

Href = Optional[AnyUrl]
Meta = Optional[MetaObject]


class Link(BaseModel):
    href: Href = Field(title="Href")
    meta: Meta = Field(title="Meta")

    @root_validator
    def check_all_values(cls, values: dict) -> dict:
        # More about these restrictions: https://jsonapi.org/format/#document-links
        if len(values) < 1:
            raise ValueError("A link object can contain the following members: href, meta.")
        return values


Links = Dict[str, Union[AnyUrl, Link, None]]

__all__ = ["Link"]
