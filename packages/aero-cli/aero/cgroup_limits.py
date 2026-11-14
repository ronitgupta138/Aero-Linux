"""
Linux cgroups v2 Resource Hierarchy & Limit Parser.
Parses memory.max, cpu.max, and formats byte quotas.
"""

def parse_cgroup_memory_limit(raw_value: str) -> int | None:
    """Parse memory.max value. Returns None if value is 'max' (unlimited)."""
    val = raw_value.strip().lower()
    if val == "max" or not val:
        return None
    try:
        return int(val)
    except ValueError:
        return None

def format_bytes(bytes_count: int | None) -> str:
    """Format raw byte counts to human readable GiB/MiB."""
    if bytes_count is None:
        return "Unlimited"
    if bytes_count < 1024:
        return f"{bytes_count} B"
    elif bytes_count < 1024 * 1024:
        return f"{bytes_count / 1024:.1f} KiB"
    elif bytes_count < 1024 * 1024 * 1024:
        return f"{bytes_count / (1024 * 1024):.1f} MiB"
    else:
        return f"{bytes_count / (1024 * 1024 * 1024):.2f} GiB"

def calculate_cpu_quota_percent(quota_us: str | int, period_us: str | int = 100000) -> float | None:
    """Calculate CPU quota percentage from cpu.max (quota period)."""
    if str(quota_us).strip().lower() == "max":
        return None
    try:
        q = float(quota_us)
        p = float(period_us)
        if p <= 0:
            return None
        return round((q / p) * 100.0, 1)
    except ValueError:
        return None
