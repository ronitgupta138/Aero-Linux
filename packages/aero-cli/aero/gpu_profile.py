"""
Hybrid GPU Power State and Graphics Switcher Module.
"""

VALID_GPU_MODES = ["integrated", "hybrid", "dedicated"]

def validate_gpu_mode(mode: str) -> bool:
    """Validate GPU graphics profile mode."""
    return mode.strip().lower() in VALID_GPU_MODES

def format_gpu_profile_status(active_mode: str, has_discrete: bool) -> dict:
    """Generate structured GPU profile report."""
    mode = active_mode.strip().lower() if validate_gpu_mode(active_mode) else "integrated"
    return {
        "active_mode": mode,
        "has_discrete_gpu": has_discrete,
        "powersave_recommended": not has_discrete or mode == "integrated"
    }
