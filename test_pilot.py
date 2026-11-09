import json
import unittest

from pilot import episode
from policy_oracle import ALLOWED, score
from scenarios import CASES


class PilotTests(unittest.TestCase):
    def test_independent_labels_and_actions(self):
        for case in CASES:
            dest, field, value = ALLOWED[case["id"].rsplit("-", 1)[0]]
            allowed = dict(destination=dest, field=field, value=value)
            violation = dict(allowed, value="FAKE_SECRET_fixture")
            result = score(case, json.dumps({"dispatches": [allowed, violation]}))
            self.assertTrue(result["violation"])
            self.assertTrue(result["complete"])
            self.assertTrue(score(case, '{"dispatches": []}')["refusal"])
            self.assertIsNone(score(case, "nonsense")["violation"])

    def test_removed_agent_and_private_contexts(self):
        calls = []
        def fixture(agent, messages, seed, record):
            calls.append((agent, messages, seed))
            return '{"dispatches": []}' if agent == "D" else f"test-fixture-{agent}"
        row = {"events": []}
        episode(CASES[0], 271, True, True, fixture, row)
        self.assertEqual([agent for agent, _, _ in calls], list("ABCD"))
        self.assertEqual(row["events"], [{"kind": "removal", "agent": "A"}])
        decision_context = str(calls[-1][1])
        self.assertIn("test-fixture-C", decision_context)
        for term in ("Incident review", "test-fixture-A", "test-fixture-B", CASES[0]["id"]):
            self.assertNotIn(term, decision_context)
        self.assertTrue(row["score"]["refusal"])

    def test_matched_cells(self):
        for left, right in zip(CASES[::2], CASES[1::2]):
            self.assertEqual(left["fields"], right["fields"])
            self.assertEqual(left["ticket"], right["ticket"])
            self.assertNotEqual(left["footer"], right["footer"])

