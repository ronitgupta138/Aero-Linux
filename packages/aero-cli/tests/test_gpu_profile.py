import unittest
from aero.gpu_profile import validate_gpu_mode, format_gpu_profile_status

class TestGpuProfile(unittest.TestCase):
    def test_validate_gpu_mode(self):
        self.assertTrue(validate_gpu_mode("integrated"))
        self.assertTrue(validate_gpu_mode("HYBRID"))
        self.assertTrue(validate_gpu_mode("dedicated"))
        self.assertFalse(validate_gpu_mode("extreme"))

    def test_format_gpu_profile_status(self):
        rep = format_gpu_profile_status("integrated", True)
        self.assertEqual(rep["active_mode"], "integrated")
        self.assertTrue(rep["powersave_recommended"])
