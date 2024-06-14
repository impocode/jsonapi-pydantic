import pytest
from pydantic import ValidationError

from jsonapi_pydantic.v1_0 import Resource, ResourceIdentifier, TopLevel


def test_toplevel_serialization(external_data: dict) -> None:
    TopLevel(**external_data)


def test_toplevel_deserialization(external_data: dict) -> None:
    top_level = TopLevel(**external_data)
    dump = top_level.model_dump(exclude_unset=True)
    assert isinstance(dump, dict)


def test_toplevel_unique_resource() -> None:
    with pytest.raises(
        ValidationError,
        match="A compound document MUST NOT include more than one resource object for each type and id pair.",
    ):
        TopLevel(
            data=[
                Resource(
                    type="articles",
                    id="3",
                    attributes={
                        "title": "JSON:API paints my bikeshed!",
                        "body": "The shortest article. Ever.",
                        "created": "2015-05-22T14:56:29.000Z",
                        "updated": "2015-05-22T14:56:28.000Z",
                    },
                ),
                Resource(
                    type="articles",
                    id="3",
                    attributes={
                        "title": "JSON:API paints my bikeshed!",
                        "body": "The shortest article. Ever.",
                        "created": "2015-05-22T14:56:29.000Z",
                        "updated": "2015-05-22T14:56:28.000Z",
                    },
                ),
            ]
        )


def test_toplevel_unique_resource_identifier() -> None:
    with pytest.raises(
        ValidationError,
        match="A compound document MUST NOT include more than one resource object for each type and id pair.",
    ):
        TopLevel(
            data=[
                ResourceIdentifier(type="articles", id="3"),
                ResourceIdentifier(type="articles", id="3"),
            ]
        )
