import hashlib
import json
import math

def validate_hash_input(value):
    if value is None:
        return "INVALID_INPUT"

    if type(value) is bool:
        return "INVALID_INPUT"

    if type(value) in (int, float):
        if not math.isfinite(float(value)):
            return "INVALID_INPUT"
        return "VALID_INPUT"

    if type(value) is str:
        return "VALID_INPUT"

    if type(value) is list:
        statuses = [validate_hash_input(v) for v in value]
        return "INVALID_INPUT" if "INVALID_INPUT" in statuses else "VALID_INPUT"

    if type(value) is tuple:
        return "INVALID_INPUT"

    if type(value) is dict:
        for key, item in value.items():
            if type(key) is not str:
                return "INVALID_INPUT"
            if validate_hash_input(item) != "VALID_INPUT":
                return "INVALID_INPUT"
        return "VALID_INPUT"

    return "INVALID_INPUT"


def hash_same_runtime(value):
    status = validate_hash_input(value)
    if status != "VALID_INPUT":
        return {"status": status, "hash": None}

    try:
        serialized = json.dumps(
            value,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ":"),
            allow_nan=False
        )
        digest = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
    except (TypeError, ValueError, OverflowError):
        return {"status": "INVALID_INPUT", "hash": None}

    return {
        "status": "ARITHMETIC_ONLY",
        "hash": digest
    }
