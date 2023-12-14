"""
Example from: https://jsonapi.org/examples/#sparse-fieldsets
"""

from jsonapi_pydantic.v1_0 import Relationship, Resource, ResourceIdentifier, TopLevel

# Example 1:
expected_data = {
    "data": [
        {
            "type": "articles",
            "id": "1",
            "attributes": {
                "title": "JSON:API paints my bikeshed!",
                "body": "The shortest article. Ever.",
                "created": "2015-05-22T14:56:29.000Z",
                "updated": "2015-05-22T14:56:28.000Z",
            },
            "relationships": {"author": {"data": {"id": "42", "type": "people"}}},
        }
    ],
    "included": [
        {"type": "people", "id": "42", "attributes": {"name": "John", "age": 80, "gender": "male"}}
    ],
}

assert expected_data == TopLevel(**expected_data), "Objects are not equal."

data = [
    Resource(
        type="articles",
        id="1",
        attributes={
            "title": "JSON:API paints my bikeshed!",
            "body": "The shortest article. Ever.",
            "created": "2015-05-22T14:56:29.000Z",
            "updated": "2015-05-22T14:56:28.000Z",
        },
        relationships={"author": Relationship(data=ResourceIdentifier(id="42", type="people"))},
    )
]
included = [
    Resource(type="people", id="42", attributes={"name": "John", "age": 80, "gender": "male"})
]
top_level = TopLevel(data=data, included=included)


assert expected_data == top_level.model_dump(exclude_unset=True), "Objects are not equal."

# Example 2:
expected_data = {
    "data": [
        {
            "type": "articles",
            "id": "1",
            "attributes": {
                "title": "JSON:API paints my bikeshed!",
                "body": "The shortest article. Ever.",
            },
            "relationships": {"author": {"data": {"id": "42", "type": "people"}}},
        }
    ],
    "included": [{"type": "people", "id": "42", "attributes": {"name": "John"}}],
}

data = [
    Resource(
        type="articles",
        id="1",
        attributes={
            "title": "JSON:API paints my bikeshed!",
            "body": "The shortest article. Ever.",
        },
        relationships={"author": {"data": {"id": "42", "type": "people"}}},
    )
]
included = [Resource(type="people", id="42", attributes={"name": "John"})]
top_level = TopLevel(data=data, included=included)

assert expected_data == top_level.model_dump(exclude_unset=True), "Objects are not equal."

# Example 3:
expected_data = {
    "data": [
        {
            "type": "articles",
            "id": "1",
            "attributes": {
                "title": "JSON:API paints my bikeshed!",
                "body": "The shortest article. Ever.",
            },
        }
    ],
    "included": [{"type": "people", "id": "42", "attributes": {"name": "John"}}],
}

data = [
    Resource(
        type="articles",
        id="1",
        attributes={
            "title": "JSON:API paints my bikeshed!",
            "body": "The shortest article. Ever.",
        },
    )
]
included = [Resource(type="people", id="42", attributes={"name": "John"})]
top_level = TopLevel(data=data, included=included)

assert expected_data == top_level.model_dump(exclude_unset=True), "Objects are not equal."
