# Ephemeral MicroVM Isolation Specification

## 1. Overview
The Aero Linux MicroVM Isolation layer orchestrates ephemeral, ultra-lightweight virtualized environments using KVM and minimal QEMU/microvm machine configurations. Designed for sandboxed script execution, untrusted artifact analysis, and isolated build runs.

## 2. Storage & RootFS Lifecycle
- **Base RootFS:** Immutable, read-only SquashFS container image holding minimal base userspace and standard development tools.
- **Copy-on-Write Layer:** Mounted via Linux `overlayfs` using a memory-backed `tmpfs` upperdir.
- **Teardown Invariant:** On microVM shutdown, the tmpfs upperdir is immediately unmounted and discarded, guaranteeing 100% state sanitization with zero residual disk persistence.

## 3. Boot & Networking Protocol
- Direct kernel boot via uncompressed `vmlinux` image with initramfs bypass, achieving cold boot times `< 120ms`.
- Host-to-guest networking through point-to-point TAP devices with private IPv4 `/30` subnets and automated NAT forwarding.
