import unittest
from aero.cpu_governor import is_valid_governor, recommend_governor_for_power

class TestCpuGovernor(unittest.TestCase):
    def test_valid_governors(self):
        self.assertTrue(is_valid_governor("powersave"))
        self.assertTrue(is_valid_governor("performance"))
        self.assertTrue(is_valid_governor("schedutil"))
        self.assertFalse(is_valid_governor("turbo_max"))

    def test_recommendation(self):
        self.assertEqual(recommend_governor_for_power(True), "powersave")
        self.assertEqual(recommend_governor_for_power(False), "performance")
