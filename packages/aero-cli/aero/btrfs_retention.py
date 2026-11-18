"""
Btrfs Snapshot Pruning and Retention Policy Evaluator.
"""

def evaluate_snapshot_pruning(snapshot_count: int, max_keep: int = 10) -> int:
    """Calculate the number of stale snapshots eligible for deletion."""
    if snapshot_count < 0 or max_keep < 0:
        raise ValueError("Counts cannot be negative")
    return max(0, snapshot_count - max_keep)
