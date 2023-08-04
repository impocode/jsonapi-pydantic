from typing import Any, Optional, Union

from pydantic.fields import Field
from pydantic.main import BaseModel
from pydantic.networks import AnyUrl

from jsonapi_pydantic.v1_0.links import Link
from jsonapi_pydantic.v1_0.meta import Meta as MetaObject


class ErrorLinks(BaseModel):
    about: Union[AnyUrl, Link] = Field(title="About")


Pointer = Optional[str]
Parameter = Optional[str]


class Source(BaseModel):
    pointer: Pointer = Field(None, title="Pointer")
    parameter: Parameter = Field(None, title="Parameter")


class Error(BaseModel):
    id: Optional[Any] = Field(None, title="Id")
    links: Optional[ErrorLinks] = Field(None, title="Links")
    status: Optional[Union[str, int]] = Field(None, title="Status")
    code: Optional[str] = Field(None, title="Code")
    title: Optional[str] = Field(None, title="Title")
    detail: Optional[str] = Field(None, title="Detail")
    source: Optional[Source] = Field(None, title="Source")
    meta: Optional[MetaObject] = Field(None, title="Meta")


__all__ = ["ErrorLinks", "Source", "Error"]
