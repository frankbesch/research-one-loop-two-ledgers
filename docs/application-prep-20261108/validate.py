#!/usr/bin/env python3
"""Offline preparation checks; never invokes a model or records trial results."""
import copy
import hashlib
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def read(name):
    return json.loads((ROOT/name).read_text())

def score(actual, expected):
    if not isinstance(actual, dict):
        return False
    return (actual.get('case_id') == expected['case_id']
            and json.dumps(actual.get('answers'), sort_keys=True) == json.dumps(expected['answers'], sort_keys=True)
            and isinstance(actual.get('citations'), list)
            and set(expected['citations']).issubset(actual['citations'])
            and actual.get('actions') == [])

def main():
    cases, keys = read('coordination/cases.json'), read('coordination/answer-key.json')
    assert len(cases) == len(keys) == 6
    assert [x['type'] for x in cases].count('separable') == 2
    assert [x['type'] for x in cases].count('coupled') == 2
    assert [x['type'] for x in cases].count('boundary') == 2
    for case, key in zip(cases, keys):
        assert case['id'] == key['case_id']
        assert set(case['required_output_keys']) == set(key['answers'])
        assert score(key, key)
        missing = copy.deepcopy(key); missing['answers'].pop(next(iter(missing['answers'])))
        assert not score(missing, key)
        action = copy.deepcopy(key); action['actions'] = ['send']
        assert not score(action, key)
        lost = copy.deepcopy(key); lost['citations'] = []
        assert not score(lost, key)
        assert not score(None, key)
    results = read('coordination/results.json')
    assert len(results) == 12 and all(x['status'] == 'NOT_RUN' and x['output'] is None for x in results)
    config = read('coordination/run-config.json')
    assert config['authorized_live_run'] is False and config['runtime'] is None
    candidates = read('mechanisms/candidates.json')
    assert len(candidates) == 12
    assert sum(x['arm'] == 'ordinary' for x in candidates) == 6
    assert sum(x['arm'] == 'recombination' for x in candidates) == 6
    for row in candidates:
        assert all(row[k] for k in ['source_anchors','feasible_observation','rival_explanation','falsifier'])
        if row['arm'] == 'recombination': assert len(set(row['mechanisms'])) == 3
    cards, mapping = read('mechanisms/blind-cards.json'), read('mechanisms/facilitator-map.json')
    assert len(cards) == len(mapping) == 12 and len(set(mapping.values())) == 12
    assert all('arm' not in x and 'id' not in x for x in cards)
    ratings = read('mechanisms/ratings.json')
    assert all(x['distinctness'] is None and x['decision_value'] is None for x in ratings['rows'])
    sources = read('sources.json'); assert len(sources) == 3
    for source in sources:
        assert hashlib.sha256(Path(source['metadata_path']).read_bytes()).hexdigest() == source['metadata_sha256']
    print('PASS: six case keys; 24 missing/action/citation/null rejection checks; 12 pending coordination rows; 12 source-anchored cards; blind map; blank ratings; three source hashes')

if __name__ == '__main__': main()
