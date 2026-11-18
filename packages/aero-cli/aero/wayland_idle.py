"""
Wayland Idle Inhibitor State Controller.
Prevents screen blanking during long build runs and presentation mode.
"""

class WaylandIdleInhibitor:
    def __init__(self):
        self._inhibited = False

    def inhibit(self):
        self._inhibited = True

    def release(self):
        self._inhibited = False

    def is_inhibited(self) -> bool:
        return self._inhibited
