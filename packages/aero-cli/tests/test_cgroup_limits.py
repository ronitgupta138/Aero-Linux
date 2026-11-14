import unittest
from aero.cgroup_limits import parse_cgroup_memory_limit, format_bytes, calculate_cpu_quota_percent

class TestCgroupLimits(unittest.TestCase):
    def test_parse_cgroup_memory_limit(self):
        self.assertIsNone(parse_cgroup_memory_limit("max"))
        self.assertIsNone(parse_cgroup_memory_limit(""))
        self.assertEqual(parse_cgroup_memory_limit("1073741824"), 1073741824)

    def test_format_bytes(self):
        self.assertEqual(format_bytes(None), "Unlimited")
        self.assertEqual(format_bytes(512), "512 B")
        self.assertEqual(format_bytes(1048576), "1.0 MiB")
        self.assertEqual(format_bytes(2147483648), "2.00 GiB")

    def test_calculate_cpu_quota_percent(self):
        self.assertIsNone(calculate_cpu_quota_percent("max", 100000))
        self.assertEqual(calculate_cpu_quota_percent(50000, 100000), 50.0)
        self.assertEqual(calculate_cpu_quota_percent(200000, 100000), 200.0)

if __name__ == "__main__":
    unittest.main()
