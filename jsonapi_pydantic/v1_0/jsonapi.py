from typing import Optional

from pydantic import BaseModel, Field

from jsonapi_pydantic.v1_0.meta import Meta as MetaObject

Version = Optional[str]
Meta = Optional[MetaObject]


class JsonApi(BaseModel):
    version: Version = Field(title="Version")
    meta: Meta = Field(title="Meta")


__all__ = ["JsonApi"]
