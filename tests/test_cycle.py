"""
Tests for Entropy Folding Engine stubs.
License: AGPLv3 (see LICENSE).
"""

from src import efe


def test_run_cycle_noop():
    items = [{"id": 1, "text": "example"}]
    result = efe.run_cycle(items, capacity=1.0)
    assert result["vault_size"] == 1
    assert result["capacity"] == 1.0  # delta is zero in stub
    assert result["insights"]
