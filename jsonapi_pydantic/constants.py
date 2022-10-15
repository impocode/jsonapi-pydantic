from dataclasses import dataclass


@dataclass
class JsonApiVersion:
    v1_0 = "1.0"
    v1_1 = "1.1"


JSON_API_VERSION = JsonApiVersion
JSON_API_MEDIA_TYPE = "application/vnd.api+json"

__all__ = ["JSON_API_MEDIA_TYPE"]
