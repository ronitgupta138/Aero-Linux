"""
NVMe Autonomous Power State Transitions (APST) Analyzer & Tuning Helper.
Calculates power state budgets and generates kernel cmdline parameters.
"""

def calculate_apst_latency_mask(max_latency_us: int) -> int:
    """Calculate the maximum allowable latency threshold in microseconds."""
    if not isinstance(max_latency_us, int) or max_latency_us < 0:
        raise ValueError("max_latency_us must be a non-negative integer.")
    return max_latency_us

def format_kernel_param(max_latency_us: int = 25000) -> str:
    """Return the kernel command line parameter for NVMe APST max latency."""
    us = calculate_apst_latency_mask(max_latency_us)
    return f"nvme_core.default_ps_max_latency_us={us}"

def parse_power_states(states: list) -> list[dict]:
    """Parse raw NVMe power states list and categorize operational vs idle states."""
    parsed = []
    for s in states:
        ps_id = s.get("id", 0)
        max_power = s.get("max_power_mw", 0)
        entry_latency = s.get("entry_latency_us", 0)
        exit_latency = s.get("exit_latency_us", 0)
        non_operational = s.get("non_operational", False)
        parsed.append({
            "id": ps_id,
            "max_power_mw": max_power,
            "total_latency_us": entry_latency + exit_latency,
            "is_idle_state": non_operational or (entry_latency + exit_latency > 5000)
        })
    return parsed
