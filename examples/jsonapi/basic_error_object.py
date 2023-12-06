"""
Example from: https://jsonapi.org/examples/#error-objects-basics
"""

from jsonapi_pydantic.v1_0 import Error, TopLevel

expected_data = {
    "errors": [
        {
            "status": "422",
            "source": {"pointer": "/data/attributes/firstName"},
            "title": "Invalid Attribute",
            "detail": "First name must contain at least two characters.",
        }
    ]
}

errors = [
    Error(
        **{
            "status": "422",
            "source": {"pointer": "/data/attributes/firstName"},
            "title": "Invalid Attribute",
            "detail": "First name must contain at least two characters.",
        }
    )
]
top_level = TopLevel(errors=errors)

assert expected_data == top_level.model_dump(exclude_unset=True), "Objects are not equal."
