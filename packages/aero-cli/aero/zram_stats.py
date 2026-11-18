"""
zRAM Compaction Ratio & Memory Compaction Statistics Collector.
"""

def parse_zram_stat_line(line: str) -> dict:
    """Parse /sys/block/zram0/mm_stat line containing 7 whitespace-separated values."""
    parts = line.strip().split()
    if len(parts) < 3:
        return {"orig_data_size": 0, "compr_data_size": 0, "compression_ratio": 1.0}
    try:
        orig = int(parts[0])
        compr = int(parts[1])
        ratio = (orig / compr) if compr > 0 else 1.0
        return {
            "orig_data_size": orig,
            "compr_data_size": compr,
            "compression_ratio": round(ratio, 2)
        }
    except (ValueError, ZeroDivisionError):
        return {"orig_data_size": 0, "compr_data_size": 0, "compression_ratio": 1.0}
