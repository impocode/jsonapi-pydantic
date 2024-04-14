from collections.abc import Hashable
from typing import Optional

from pydantic.config import ConfigDict
from pydantic.fields import Field
from pydantic.main import BaseModel

from jsonapi_pydantic.utils import _generate_resource_hash
from jsonapi_pydantic.v1_0.meta import Meta as MetaObject

Meta = Optional[MetaObject]


class ResourceIdentifier(BaseModel, Hashable):
    id: str = Field(title="Id")
    type: str = Field(title="Type")
    meta: Meta = Field(None, title="Meta")

    model_config = ConfigDict(frozen=True)

    _hash: int

    def __init__(self, **data):
        super().__init__(**data)
        self._hash = _generate_resource_hash(resource_type=self.type, resource_id=self.id)

    def __eq__(self, __value: object) -> bool:
        return self._hash == getattr(__value, "_hash", None)

    def __hash__(self) -> int:
        return self._hash


__all__ = ["ResourceIdentifier"]
