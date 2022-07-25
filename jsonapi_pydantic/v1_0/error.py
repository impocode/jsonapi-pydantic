from typing import Any, Optional, Union

from pydantic import AnyUrl, BaseModel, Field

from jsonapi_pydantic.v1_0.links import Link
from jsonapi_pydantic.v1_0.meta import Meta as MetaObject


class ErrorLinks(BaseModel):
    about: Union[AnyUrl, Link] = Field(title="About")


Pointer = Optional[str]
Parameter = Optional[str]


class Source(BaseModel):
    pointer: Pointer = Field(title="Pointer")
    parameter: Parameter = Field(title="Parameter")


Id = Optional[Any]
Status = Optional[str]
Code = Optional[str]
Title = Optional[str]
Detail = Optional[str]
Meta = Optional[MetaObject]


class Error(BaseModel):
    id: Id = Field(title="Id")
    links: Optional[ErrorLinks] = Field(title="Links")
    status: Status = Field(title="Status")
    code: Code = Field(title="Code")
    title: Title = Field(title="Title")
    detail: Detail = Field(title="Detail")
    source: Optional[Source] = Field(title="Source")
    meta: Meta = Field(title="Meta")


__all__ = ["ErrorLinks", "Source", "Error"]
