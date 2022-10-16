from typing import Any, Dict, Optional

from pydantic import BaseModel, Field, root_validator

from jsonapi_pydantic.v1_0.links import Links as LinksObject
from jsonapi_pydantic.v1_0.meta import Meta as MetaObject
from jsonapi_pydantic.v1_0.resource.relationship import Relationship

Id = Optional[str]
Attributes = Optional[Dict[str, Any]]
Relationships = Optional[Dict[str, Relationship]]
Links = Optional[LinksObject]
Meta = Optional[MetaObject]


class Resource(BaseModel):
    type: str = Field(title="Type")
    id: Id = Field(title="Id")
    attributes: Attributes = Field(title="Attributes")
    relationships: Relationships = Field(title="Relationships")
    links: Links = Field(title="Links")
    meta: Meta = Field(title="Meta")

    @root_validator
    def check_all_values(cls, values: dict) -> dict:
        attributes, relationships = values.get("attributes"), values.get("relationships")
        if not attributes and not relationships:
            return values

        # More about these restrictions: https://jsonapi.org/format/#document-resource-object-fields
        try:
            attributes = dict(attributes) if attributes else attributes
            relationships = dict(relationships) if relationships else relationships
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

        return values


__all__ = ["Resource"]
