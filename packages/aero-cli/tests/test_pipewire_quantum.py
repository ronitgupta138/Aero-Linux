import unittest
from aero.pipewire_quantum import (
    is_valid_quantum,
    calculate_roundtrip_latency_ms,
    generate_wireplumber_config,
    VALID_QUANTUMS
)

class TestPipewireQuantum(unittest.TestCase):
    def test_is_valid_quantum(self):
        for q in VALID_QUANTUMS:
            self.assertTrue(is_valid_quantum(q))
        self.assertFalse(is_valid_quantum(48))
        self.assertFalse(is_valid_quantum(2048))

    def test_calculate_roundtrip_latency_ms(self):
        latency_64 = calculate_roundtrip_latency_ms(64, 48000)
        self.assertAlmostEqual(latency_64, 1.333, places=2)
        latency_128 = calculate_roundtrip_latency_ms(128, 48000)
        self.assertAlmostEqual(latency_128, 2.667, places=2)

    def test_generate_wireplumber_config(self):
        cfg = generate_wireplumber_config(64, 48000)
        self.assertEqual(cfg["context.properties"]["default.clock.quantum"], 64)
        self.assertAlmostEqual(cfg["latency_ms"], 1.333, places=2)

if __name__ == "__main__":
    unittest.main()
