import unittest
from aero.nvme_apst import calculate_apst_latency_mask, format_kernel_param, parse_power_states

class TestNVMeAPST(unittest.TestCase):
    def test_calculate_apst_latency_mask(self):
        self.assertEqual(calculate_apst_latency_mask(25000), 25000)
        with self.assertRaises(ValueError):
            calculate_apst_latency_mask(-1)

    def test_format_kernel_param(self):
        self.assertEqual(format_kernel_param(25000), "nvme_core.default_ps_max_latency_us=25000")
        self.assertEqual(format_kernel_param(5000), "nvme_core.default_ps_max_latency_us=5000")

    def test_parse_power_states(self):
        raw = [
            {"id": 0, "max_power_mw": 5000, "entry_latency_us": 0, "exit_latency_us": 0, "non_operational": False},
            {"id": 3, "max_power_mw": 50, "entry_latency_us": 2000, "exit_latency_us": 6000, "non_operational": True},
        ]
        parsed = parse_power_states(raw)
        self.assertEqual(len(parsed), 2)
        self.assertFalse(parsed[0]["is_idle_state"])
        self.assertTrue(parsed[1]["is_idle_state"])
        self.assertEqual(parsed[1]["total_latency_us"], 8000)

if __name__ == "__main__":
    unittest.main()
