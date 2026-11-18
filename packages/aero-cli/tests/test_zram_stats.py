import unittest
from aero.zram_stats import parse_zram_stat_line

class TestZramStats(unittest.TestCase):
    def test_parse_valid_stat_line(self):
        # 4GB uncompressed, 1GB compressed -> 4.0x ratio
        stat_line = "4294967296 1073741824 1073741824 0 0 0 0"
        parsed = parse_zram_stat_line(stat_line)
        self.assertEqual(parsed["orig_data_size"], 4294967296)
        self.assertEqual(parsed["compr_data_size"], 1073741824)
        self.assertEqual(parsed["compression_ratio"], 4.0)

    def test_parse_empty_stat_line(self):
        parsed = parse_zram_stat_line("")
        self.assertEqual(parsed["compression_ratio"], 1.0)
