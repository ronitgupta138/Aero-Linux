"""
ASUS Embedded Controller (EC) Battery Charge Threshold Module.
Exposes sysfs hardware control and udev configuration helpers.
"""

import os

SYSFS_BAT0 = "/sys/class/power_supply/BAT0/charge_control_end_threshold"

def validate_threshold(threshold: int) -> bool:
    """Validate charge threshold percentage (50-100%)."""
    return isinstance(threshold, int) and 50 <= threshold <= 100

def get_battery_threshold_path(sysfs_root: str = "/sys/class/power_supply/BAT0") -> str:
    """Return the sysfs path for battery charge control."""
    return os.path.join(sysfs_root, "charge_control_end_threshold")

def read_battery_threshold(sysfs_path: str = SYSFS_BAT0) -> dict:
    """Read the current battery charge end threshold from sysfs."""
    if not os.path.exists(sysfs_path):
        return {"supported": False, "threshold": None, "error": "Hardware endpoint not present"}
    try:
        with open(sysfs_path, "r", encoding="utf-8") as f:
            val = int(f.read().strip())
        return {"supported": True, "threshold": val, "error": None}
    except Exception as e:
        return {"supported": False, "threshold": None, "error": str(e)}

def generate_udev_rule(threshold: int = 80) -> str:
    """Generate udev rule string for automatic charge capping."""
    if not validate_threshold(threshold):
        raise ValueError(f"Invalid threshold: {threshold}. Must be between 50 and 100.")
    return (
        'ACTION=="add|change", SUBSYSTEM=="power_supply", ATTR{type}=="Battery", '
        f'ATTR{{charge_control_end_threshold}}="{threshold}"\n'
    )

def generate_systemd_service(threshold: int = 80) -> str:
    """Generate systemd one-shot service unit for charge capping."""
    if not validate_threshold(threshold):
        raise ValueError(f"Invalid threshold: {threshold}. Must be between 50 and 100.")
    return f"""[Unit]
Description=ASUS Battery Charge Threshold Capper ({threshold}%)
After=multi-user.target
Documentation=https://github.com/ronitgupta138/aero-linux

[Service]
Type=oneshot
ExecStart=/bin/sh -c 'echo {threshold} > /sys/class/power_supply/BAT0/charge_control_end_threshold'
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
"""
