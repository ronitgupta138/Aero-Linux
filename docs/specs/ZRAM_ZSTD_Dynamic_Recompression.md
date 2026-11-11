# ZRAM ZSTD Dynamic Recompression Specification

## 1. Multi-Tiered Memory Compression
To maximize available RAM on memory-constrained systems, Aero Linux configures dual-algorithm zRAM pools:
- **Fast Tier (LZO-RLE):** Active pages compressed with sub-microsecond latency.
- **Deep Tier (ZSTD):** Cold, inactive pages dynamically recompressed using ZSTD (level 3), delivering up to 3.2:1 compression ratios.

## 2. Swap Writeback Mechanics
Under persistent memory pressure, non-compressible dirty pages are written back to encrypted NVMe storage with `discard` TRIM commands issued in batches.
