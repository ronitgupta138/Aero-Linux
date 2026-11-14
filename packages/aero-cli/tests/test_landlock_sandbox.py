import unittest
from aero.landlock_sandbox import (
    LandlockRulesetBuilder,
    ACCESS_FS_READ,
    ACCESS_FS_WRITE,
    ACCESS_FS_EXEC,
)

class TestLandlockSandbox(unittest.TestCase):
    def test_ruleset_builder(self):
        builder = LandlockRulesetBuilder()
        builder.allow_read("/usr")
        builder.allow_write("/tmp")
        builder.allow_exec("/usr/bin/python3")
        spec = builder.build()
        self.assertEqual(spec["rules_count"], 3)
        self.assertTrue(spec["no_new_privs"])
        self.assertEqual(spec["abi_version"], 3)
        self.assertEqual(spec["rules"][0]["access"], ACCESS_FS_READ)
        self.assertEqual(spec["rules"][1]["access"], ACCESS_FS_READ | ACCESS_FS_WRITE)
        self.assertEqual(spec["rules"][2]["access"], ACCESS_FS_READ | ACCESS_FS_EXEC)

if __name__ == "__main__":
    unittest.main()
