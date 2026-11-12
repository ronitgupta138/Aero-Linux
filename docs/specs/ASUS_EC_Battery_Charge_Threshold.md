# ASUS Embedded Controller (EC) Battery Charge Threshold Protocol

## 1. Subsystem Architecture
Aero Linux provides hardware-level battery health preservation for modern ASUS mobile workstations (ZenBook, ROG, TUF, VivoBook) by interfacing directly with the ASUS Embedded Controller (EC) via ACPI/sysfs interfaces.

## 2. Kernel Sysfs Abstraction
The battery charge control endpoint is exposed at:
`/sys/class/power_supply/BAT0/charge_control_end_threshold`

- **Permitted Threshold Range:** `50` to `100` (percentage integer).
- **Default Production Setting:** `80` (optimal lithium-ion cycle preservation).
- **Hardware Mechanism:** When battery charge reaches the designated integer percentage, the EC hardware asserts battery cut-off and transitions the power delivery controller strictly to AC bypass rail.

## 3. Udev Hardware Rule & Systemd Integration
```udev
ACTION=="add", SUBSYSTEM=="power_supply", ATTR{type}=="Battery", ATTR{charge_control_end_threshold}="80"
```
The kernel udev trigger ensures that charge capping persists across warm reboots, cold starts, and kernel updates.
