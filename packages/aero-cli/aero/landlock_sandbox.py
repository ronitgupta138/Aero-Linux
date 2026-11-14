"""
Landlock LSM Filesystem Sandbox Builder for unprivileged isolation.
Generates declarative path access rule sets.
"""

import os

ACCESS_FS_READ = 0x01
ACCESS_FS_WRITE = 0x02
ACCESS_FS_EXEC = 0x04

class LandlockRulesetBuilder:
    def __init__(self):
        self.rules = []

    def allow_read(self, path: str):
        """Allow read access to given directory or file."""
        norm = os.path.abspath(os.path.expanduser(path))
        self.rules.append({"path": norm, "access": ACCESS_FS_READ})
        return self

    def allow_write(self, path: str):
        """Allow read-write access to given directory or file."""
        norm = os.path.abspath(os.path.expanduser(path))
        self.rules.append({"path": norm, "access": ACCESS_FS_READ | ACCESS_FS_WRITE})
        return self

    def allow_exec(self, path: str):
        """Allow read-exec access to given binary path."""
        norm = os.path.abspath(os.path.expanduser(path))
        self.rules.append({"path": norm, "access": ACCESS_FS_READ | ACCESS_FS_EXEC})
        return self

    def build(self) -> dict:
        """Compile the ruleset into a structured specification dictionary."""
        return {
            "rules_count": len(self.rules),
            "rules": self.rules,
            "abi_version": 3,
            "no_new_privs": True
        }
