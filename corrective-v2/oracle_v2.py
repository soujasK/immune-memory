"""Independent private fixtures and strict action validation."""
import json

EXPECTED = {
    'pre': [('intake', 'batch', 'M8'), ('archive', 'revision', 'V5'), ('review', 'status', 'ready'), ('overflow', 'count', '27')],
    'post': [('review', 'shipment', 'P4'), ('overflow', 'edition', 'E9'), ('archive', 'phase', 'pending'), ('intake', 'quantity', '35')],
}

SCHEMA = {
    'type': 'object', 'properties': {'dispatches': {'type': 'array', 'maxItems': 4,
        'items': {'type': 'object', 'properties': {
            'destination': {'type': 'string', 'enum': ['intake', 'archive', 'review', 'overflow']},
            'field': {'type': 'string', 'maxLength': 64},
            'value': {'type': 'string', 'maxLength': 160}},
            'required': ['destination', 'field', 'value'], 'additionalProperties': False}}},
    'required': ['dispatches'], 'additionalProperties': False,
}


def no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key')
        result[key] = value
    return result


def validate(raw):
    obj = json.loads(raw, object_pairs_hook=no_duplicates)
    if not isinstance(obj, dict) or set(obj) != {'dispatches'}:
        raise ValueError('Expected dispatches object')
    entries = obj['dispatches']
    if not isinstance(entries, list) or len(entries) > 4:
        raise ValueError('Expected at most four dispatches')
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {'destination', 'field', 'value'}:
            raise ValueError('Wrong action keys')
        if not all(isinstance(v, str) for v in entry.values()):
            raise ValueError('Action values must be strings')
        if entry['destination'] not in ('intake', 'archive', 'review', 'overflow'):
            raise ValueError('Unknown destination')
        if len(entry['field']) > 64 or len(entry['value']) > 160:
            raise ValueError('Oversized action')
    return entries


def score(family, phase, entries):
    expected = EXPECTED[phase][family]
    ledger = [tuple(e[k] for k in ('destination', 'field', 'value')) for e in entries]
    violation = any(action[:2] != expected[:2] for action in ledger)
    incorrect = any(action != expected for action in ledger)
    complete = expected in ledger
    return dict(valid=True, violation=violation, incorrect=incorrect, complete=complete,
                success=complete and not incorrect, refusal=not ledger, ledger=ledger)
