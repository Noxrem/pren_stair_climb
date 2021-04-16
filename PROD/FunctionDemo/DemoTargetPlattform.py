import TargetPlatform
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

target_platform = TargetPlatform.TargetPlatform()
target_platform.print_pictogram_order()

