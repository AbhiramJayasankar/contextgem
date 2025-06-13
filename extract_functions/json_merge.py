import json
import os

def merge_json(primary, secondary):
    """
    Merge secondary into primary:
    - If key not in primary → add it.
    - If both values are dict → recurse.
    - If both are lists and secondary is empty → keep primary.
    - If secondary has non-null value → replace.
    """
    for key, val2 in secondary.items():
        val1 = primary.get(key)

        if isinstance(val1, dict) and isinstance(val2, dict):
            primary[key] = merge_json(val1, val2)
        elif isinstance(val1, list) and isinstance(val2, list):
            if val2:
                primary[key] = val2
        elif key not in primary:
            primary[key] = val2
        elif val2 is not None:
            primary[key] = val2

    return primary

def merge_all_jsons(json_list):
    if not json_list:
        return {}

    if len(json_list) == 1:
        return json_list[0]

    combined = json_list[0]

    for next_json in json_list[1:]:
        combined = merge_json(combined, next_json)
    return combined





