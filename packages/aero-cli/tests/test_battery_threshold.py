import unittest
import tempfile
import os
from aero.battery_threshold import (
    validate_threshold,
    get_battery_threshold_path,
    read_battery_threshold,
    generate_udev_rule,
    generate_systemd_service,
)

class TestBatteryThreshold(unittest.TestCase):
    def test_validate_threshold(self):
        self.assertTrue(validate_threshold(50))
        self.assertTrue(validate_threshold(80))
        self.assertTrue(validate_threshold(100))
        self.assertFalse(validate_threshold(49))
        self.assertFalse(validate_threshold(101))
        self.assertFalse(validate_threshold("80"))

    def test_get_battery_threshold_path(self):
        path = get_battery_threshold_path("/tmp/sys/test")
        self.assertEqual(path, "/tmp/sys/test/charge_control_end_threshold")

    def test_read_battery_threshold_mock(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, "charge_control_end_threshold")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("80\n")
            result = read_battery_threshold(file_path)
            self.assertTrue(result["supported"])
            self.assertEqual(result["threshold"], 80)
            self.assertIsNone(result["error"])

    def test_read_battery_threshold_missing(self):
        result = read_battery_threshold("/tmp/nonexistent_battery_sysfs_path")
        self.assertFalse(result["supported"])
        self.assertIsNone(result["threshold"])

    def test_generate_udev_rule(self):
        rule = generate_udev_rule(80)
        self.assertIn('ATTR{charge_control_end_threshold}="80"', rule)
        with self.assertRaises(ValueError):
            generate_udev_rule(40)

    def test_generate_systemd_service(self):
        unit = generate_systemd_service(80)
        self.assertIn("echo 80 >", unit)
        self.assertIn("[Install]", unit)
        with self.assertRaises(ValueError):
            generate_systemd_service(105)

if __name__ == "__main__":
    unittest.main()
