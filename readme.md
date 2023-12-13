# jsonapi-pydantic

<p align="center">
  <em><a href="https://jsonapi.org" target="_blank">JSON:API</a> implementation with <a href="https://pydantic-docs.helpmanual.io" target="_blank">Pydantic.</a>
  </em>
</p>
<p align="center">
  <a href="https://pypi.org/project/jsonapi-pydantic/" target="_blank">
      <img src="https://img.shields.io/pypi/v/jsonapi-pydantic" alt="PyPI">
  </a>
  <a href="https://github.com/impocode/jsonapi-pydantic/blob/master/license.md" target="_blank">
      <img src="https://img.shields.io/github/license/impocode/jsonapi-pydantic.svg" alt="License">
  </a>
</p>

## Description

`jsonapi-pydantic` provides a suite of Pydantic models matching the JSON:API specification.

## Install

```shell
$ pip install jsonapi-pydantic
```

Or use your python package manager.

## Usage

Object with primary data:

```python
from jsonapi_pydantic.v1_0 import TopLevel

external_data = {
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

top_level = TopLevel(**external_data)

print(top_level.model_dump(exclude_unset=True))
"""
{
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
"""
print(top_level.data)
"""
[
    Resource(
        type="articles",
        id="1",
        attributes={
            "title": "JSON:API paints my bikeshed!",
            "body": "The shortest article. Ever.",
            "created": "2015-05-22T14:56:29.000Z",
            "updated": "2015-05-22T14:56:28.000Z",
        },
        relationships={
            "author": Relationship(
                links=None, data=ResourceIdentifier(id="42", type="people", meta=None), meta=None
            )
        },
        links=None,
        meta=None,
    )
]
"""
```

## Examples

More examples can be found [here](https://github.com/impocode/jsonapi-pydantic/tree/master/examples).

## License

See [license.md](https://github.com/impocode/jsonapi-pydantic/blob/master/license.md).
