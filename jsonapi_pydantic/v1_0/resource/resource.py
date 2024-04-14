from collections.abc import Hashable
from random import getrandbits
from typing import Any, Dict, Optional

from pydantic.config import ConfigDict
from pydantic.fields import Field
from pydantic.functional_validators import model_validator
from pydantic.main import BaseModel

from jsonapi_pydantic.utils import _generate_resource_hash
from jsonapi_pydantic.v1_0.links import Links as LinksObject
from jsonapi_pydantic.v1_0.meta import Meta as MetaObject
from jsonapi_pydantic.v1_0.resource.relationship import Relationship

Id = Optional[str]
Attributes = Optional[Dict[str, Any]]
Relationships = Optional[Dict[str, Relationship]]
Links = Optional[LinksObject]
Meta = Optional[MetaObject]


class Resource(BaseModel, Hashable):
    type: str = Field(title="Type")
    id: Id = Field(None, title="Id")
    attributes: Attributes = Field(None, title="Attributes")
    relationships: Relationships = Field(None, title="Relationships")
    links: Links = Field(None, title="Links")
    meta: Meta = Field(None, title="Meta")

    model_config = ConfigDict(frozen=True)

    _hash: int

    def __init__(self, **data):
        super().__init__(**data)
        if self.id:
            self._hash = _generate_resource_hash(resource_type=self.type, resource_id=self.id)
        else:
            self._hash = getrandbits(64)

    def __eq__(self, __value: object) -> bool:
        return self._hash == getattr(__value, "_hash", None)

    def __hash__(self) -> int:
        return self._hash

    @model_validator(mode="after")
    def check_all_values(self) -> "Resource":
        if not self.attributes and not self.relationships:
            return self

        # More about these restrictions: https://jsonapi.org/format/#document-resource-object-fields
        try:
            attributes = dict(self.attributes) if self.attributes else self.attributes
            relationships = dict(self.relationships) if self.relationships else self.relationships
        except (ValueError, TypeError):
            raise ValueError("Attributes and relationships must be json objects.")

        if attributes and (attributes.get("id") or attributes.get("type")):
            raise ValueError("Attributes can not have keys named id or type.")

        if relationships and (relationships.get("id") or relationships.get("type")):
            raise ValueError("Relationships can not have keys named id or type.")

        if attributes and relationships:
            for key in attributes:
                if relationships.get(key):
                    raise ValueError(
                        f"A resource can not have an attribute and relationship with the same name. Name: {key}."
                    )

        return self


__all__ = ["Resource"]
