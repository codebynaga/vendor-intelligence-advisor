from pathlib import Path
import json
p=Path(__file__).resolve().parents[1]
d=json.loads((p/'dashboard/data.json').read_text())
assert len(d['products'])==5
assert sum(x['reviews'] for x in d['products'])==d['metrics']['demo_reviews']
assert 'Vendor Intelligence Advisor' in (p/'dashboard/index.html').read_text()
print('Snapshot consistency checks passed')
