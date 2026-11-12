# dm-verity Cryptographic Root Integrity Verification Specification

## 1. Cryptographic Block Layer Protection
Aero Linux utilizes device-mapper `dm-verity` to ensure transparent, block-by-block cryptographic integrity verification of immutable system runtime images.

## 2. Merkle Tree Architecture
- **Data Device:** Read-only ext4 or Btrfs subvolume holding root filesystem contents.
- **Hash Device:** Cryptographic SHA-256 Merkle tree holding hashes of each 4096-byte data block.
- **Root Hash:** 256-bit cryptographic root hash passed to the kernel bootloader or signed EFI stub.

## 3. Tamper Detection Invariants
Any unauthorized bit mutation or filesystem corruption triggers an immediate I/O error (`EIO`) at the block layer prior to page cache population, preventing modified binaries from executing.
