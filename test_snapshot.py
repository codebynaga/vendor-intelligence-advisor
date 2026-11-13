import json,unittest
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[1]/'dashboard'/'data.json').read_text())
class SnapshotTests(unittest.TestCase):
 def test_review_totals(self):
  self.assertEqual(sum(p['reviews'] for p in D['products']),246)
 def test_semantic_accounting(self):
  m=D['metrics'];self.assertEqual(m['semantic_selected'],m['semantic_accepted']+m['semantic_fallback'])
 def test_action_accounting(self):
  m=D['metrics'];self.assertEqual(m['actions'],m['gpt_actions']+m['fallback_actions'])
 def test_low_star_ranges(self):
  self.assertTrue(all(0<=p['low']<=100 for p in D['products']))
if __name__=='__main__':unittest.main()
