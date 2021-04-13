from unittest import TestCase
import MagnetManager


class TestMagnetManager(TestCase):
    magnet_manager = None

    def setUp(self):
        self.magnet_manager = MagnetManager.MagnetManager()

    def test_constructor(self):
        self.assertIsNotNone(self.magnet_manager)

    def test_init_state_bridge(self):
        self.assertFalse(self.magnet_manager.is_switched_on_magnet_bridge)

    def test_init_state_socket(self):
        self.assertFalse(self.magnet_manager.is_switched_on_magnet_socket)

    def test_get_available_arguments(self):
        assert True
        # TODO: tbd.

    def test_get_state_bridge(self):
        assert True
        # TODO: tbd.

    def test_set_on_power_bridge(self):
        self.magnet_manager.set_on_power_bridge()
        self.assertTrue(self.magnet_manager.is_switched_on_magnet_bridge)

    def test_set_off_power_bridge(self):
        self.magnet_manager.set_off_power_bridge()
        self.assertTrue(not self.magnet_manager.is_switched_on_magnet_bridge)

    def test_get_state_socket(self):
        assert True
        # TODO: tbd.

    def test_set_on_power_socket(self):
        self.magnet_manager.set_on_power_socket()
        self.assertTrue(self.magnet_manager.is_switched_on_magnet_socket)

    def test_set_off_power_socket(self):
        self.magnet_manager.set_off_power_socket()
        self.assertTrue(not self.magnet_manager.is_switched_on_magnet_socket)
