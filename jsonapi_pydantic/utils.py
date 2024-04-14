def _generate_resource_hash(resource_type: str, resource_id: str) -> int:
    hash_ = ""
    for ch in resource_type:
        hash_ += str(ord(ch))
    for ch in resource_id:
        hash_ += str(ord(ch))
    return int(hash_)


__all__ = ["_generate_resource_hash"]
