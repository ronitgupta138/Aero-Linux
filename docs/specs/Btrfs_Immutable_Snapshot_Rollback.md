# Btrfs Subvolume Layout & Atomic Snapshot Rollback Specification

## 1. Subvolume Architecture
- `@` (Root Filesystem): Contains the OS image, system libraries, and `/usr`.
- `@home` (User Workspace): Isolated persistent user data, preserved across OS rollbacks.
- `@snapshots`: Read-only historical filesystem states.

## 2. Atomic Rollback Algorithm
- Before system upgrades or package installations, the package manager takes a read-only snapshot:
  `btrfs subvolume snapshot -r / /@snapshots/root-$(date +%s)`
- Rollback replaces the default subvolume ID in the Btrfs root tree in $O(1)$ time, guaranteeing bootable recovery even after kernel corruption.
