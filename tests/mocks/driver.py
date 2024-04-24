from unittest.mock import MagicMock

from speed_sleuth.driver import DriverInterface


@DriverInterface.register
class MockDriver:
    def __init__(self):
        self.get = MagicMock()
        self.find_element = MagicMock()
        self.wait_to_be_visible = MagicMock()
        self.wait_for_element = MagicMock()
        self.wait_for_button_clickable = MagicMock()
        self.cleanup = MagicMock()
