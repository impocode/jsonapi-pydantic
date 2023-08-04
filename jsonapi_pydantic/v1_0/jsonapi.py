from typing import Optional

from pydantic.fields import Field
from pydantic.main import BaseModel

from jsonapi_pydantic.v1_0.meta import Meta as MetaObject

Version = Optional[str]
Meta = Optional[MetaObject]


class JsonApi(BaseModel):
    version: Version = Field(None, title="Version")
    meta: Meta = Field(None, title="Meta")


__all__ = ["JsonApi"]
