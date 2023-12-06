"""
Example from: https://jsonapi.org/examples/#error-objects-multiple-errors
"""

from jsonapi_pydantic.v1_0 import Error, TopLevel

expected_data = {
    "errors": [
        {
            "status": "403",
            "source": {"pointer": "/data/attributes/secretPowers"},
            "detail": "Editing secret powers is not authorized on Sundays.",
        },
        {
            "status": "422",
            "source": {"pointer": "/data/attributes/volume"},
            "detail": "Volume does not, in fact, go to 11.",
        },
        {
            "status": "500",
            "source": {"pointer": "/data/attributes/reputation"},
            "title": "The backend responded with an error",
            "detail": "Reputation service not responding after three requests.",
        },
    ]
}

errors = [
    Error(
        **{
            "status": "403",
            "source": {"pointer": "/data/attributes/secretPowers"},
            "detail": "Editing secret powers is not authorized on Sundays.",
        }
    ),
    Error(
        **{
            "status": "422",
            "source": {"pointer": "/data/attributes/volume"},
            "detail": "Volume does not, in fact, go to 11.",
        }
    ),
    Error(
        **{
            "status": "500",
            "source": {"pointer": "/data/attributes/reputation"},
            "title": "The backend responded with an error",
            "detail": "Reputation service not responding after three requests.",
        }
    ),
]
top_level = TopLevel(errors=errors)

assert expected_data == top_level.model_dump(exclude_unset=True), "Objects are not equal."
