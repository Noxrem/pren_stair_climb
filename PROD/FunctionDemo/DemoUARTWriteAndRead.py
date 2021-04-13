import UARTAccess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


access = UARTAccess.UARTAccess()
access.write_and_read("drv help")
