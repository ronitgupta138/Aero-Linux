import unittest
from aero.wayland_idle import WaylandIdleInhibitor

class TestWaylandIdle(unittest.TestCase):
    def test_inhibit_lifecycle(self):
        inhibitor = WaylandIdleInhibitor()
        self.assertFalse(inhibitor.is_inhibited())
        inhibitor.inhibit()
        self.assertTrue(inhibitor.is_inhibited())
        inhibitor.release()
        self.assertFalse(inhibitor.is_inhibited())
