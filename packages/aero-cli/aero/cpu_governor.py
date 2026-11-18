"""
Linux CPU Governor and Frequency Scaling Reader.
"""

VALID_GOVERNORS = ["powersave", "performance", "schedutil", "ondemand", "conservative"]

def is_valid_governor(governor: str) -> bool:
    return governor.strip().lower() in VALID_GOVERNORS

def recommend_governor_for_power(on_battery: bool) -> str:
    return "powersave" if on_battery else "performance"
