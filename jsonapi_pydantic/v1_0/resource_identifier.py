from typing import Optional

from pydantic.fields import Field
from pydantic.main import BaseModel

from jsonapi_pydantic.v1_0.meta import Meta as MetaObject

Meta = Optional[MetaObject]


class ResourceIdentifier(BaseModel):
    id: str = Field(title="Id")
    type: str = Field(title="Type")
    meta: Meta = Field(None, title="Meta")


__all__ = ["ResourceIdentifier"]
