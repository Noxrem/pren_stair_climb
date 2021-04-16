import MagnetManager
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

magnet_manager = MagnetManager.MagnetManager()
magnet_manager.set_on_power_bridge()
time.sleep(3)
magnet_manager.set_off_power_bridge()
time.sleep(3)
magnet_manager.set_on_power_socket()
time.sleep(3)
magnet_manager.set_off_power_socket()
