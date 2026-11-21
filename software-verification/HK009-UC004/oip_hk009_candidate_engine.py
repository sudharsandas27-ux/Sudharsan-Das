import math
from collections.abc import Mapping

WEIGHTS = {
    "SCORE": {"OE": 0.6, "CV": 0.3, "VIS": 0.1},
    "SIS": {"RC": 0.5, "AFL": 0.3, "CAS": 0.2},
}

STATUSES = {
    "CALCULATED",
    "ARITHMETIC_ONLY",
    "PENDING_EVIDENCE",
    "INVALID_INPUT",
    "UNDEFINED",
}

def validate_numeric(value):
    if value is None:
        return "PENDING_EVIDENCE"
    if type(value) not in (int, float):
        return "INVALID_INPUT"
    try:
        if not math.isfinite(float(value)):
            return "INVALID_INPUT"
    except (TypeError, ValueError, OverflowError):
        return "INVALID_INPUT"
    return "VALID_INPUT"

def validate_ids(ids):
    status = validate_numeric(ids)
    if status != "VALID_INPUT":
        return status
    if not 0 <= ids <= 1:
        return "INVALID_INPUT"
    return "VALID_INPUT"

def _result(status, value=None):
    if status not in STATUSES:
        return {"status": "INVALID_INPUT", "result": None}
    if status in ("CALCULATED", "ARITHMETIC_ONLY"):
        if type(value) not in (int, float) or not math.isfinite(float(value)):
            return {"status": "INVALID_INPUT", "result": None}
    else:
        value = None
    return {"status": status, "result": value}

def _finite_result(value):
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError, OverflowError):
        return False

def calculate_weighted_formula(inputs, weights):
    if not isinstance(inputs, Mapping) or not isinstance(weights, Mapping):
        return _result("INVALID_INPUT")
    if not weights:
        return _result("INVALID_INPUT")

    for key, weight in weights.items():
        if not isinstance(key, str) or not key:
            return _result("INVALID_INPUT")
        if validate_numeric(weight) != "VALID_INPUT":
            return _result("INVALID_INPUT")

    statuses = [validate_numeric(inputs.get(key)) for key in weights]

    if "INVALID_INPUT" in statuses:
        return _result("INVALID_INPUT")
    if "PENDING_EVIDENCE" in statuses:
        return _result("PENDING_EVIDENCE")

    try:
        value = sum(inputs[key] * weights[key] for key in weights)
    except (TypeError, ValueError, OverflowError, ArithmeticError):
        return _result("INVALID_INPUT")

    if not _finite_result(value):
        return _result("INVALID_INPUT")
    return _result("ARITHMETIC_ONLY", value)

def calculate_score(oe, cv, vis):
    return calculate_weighted_formula(
        {"OE": oe, "CV": cv, "VIS": vis},
        WEIGHTS["SCORE"]
    )

def calculate_sis(rc, afl, cas):
    return calculate_weighted_formula(
        {"RC": rc, "AFL": afl, "CAS": cas},
        WEIGHTS["SIS"]
    )

def calculate_ii(ids):
    status = validate_ids(ids)
    if status != "VALID_INPUT":
        return _result(status)
    return _result("ARITHMETIC_ONLY", 1 - ids)

def calculate_liv(ri, sr, ar, ids):
    ids_status = validate_ids(ids)
    if ids_status != "VALID_INPUT":
        return _result(ids_status)
    if ids == 0:
        return _result("UNDEFINED")

    statuses = [validate_numeric(v) for v in (ri, sr, ar)]
    if "INVALID_INPUT" in statuses:
        return _result("INVALID_INPUT")
    if "PENDING_EVIDENCE" in statuses:
        return _result("PENDING_EVIDENCE")

    try:
        value = (ri * sr * ar) / ids
    except (ArithmeticError, TypeError, ValueError, OverflowError):
        return _result("INVALID_INPUT")

    if not _finite_result(value):
        return _result("INVALID_INPUT")
    return _result("ARITHMETIC_ONLY", value)

def calculate_oip_stability(gfl, ids, aml):
    statuses = [
        validate_numeric(gfl),
        validate_ids(ids),
        validate_numeric(aml)
    ]
    if "INVALID_INPUT" in statuses:
        return _result("INVALID_INPUT")
    if "PENDING_EVIDENCE" in statuses:
        return _result("PENDING_EVIDENCE")

    try:
        value = gfl * (1 - ids) * aml
    except (ArithmeticError, TypeError, ValueError, OverflowError):
        return _result("INVALID_INPUT")

    if not _finite_result(value):
        return _result("INVALID_INPUT")
    return _result("ARITHMETIC_ONLY", value)
