from typing import Optional

from pydantic import BaseModel, Field

from jsonapi_pydantic.v1_0.meta import Meta as MetaObject

Meta = Optional[MetaObject]


class ResourceIdentifier(BaseModel):
    id: str = Field(title="Id")
    type: str = Field(title="Type")
    meta: Meta = Field(title="Meta")


__all__ = ["ResourceIdentifier"]
