import logging
import os
from config.config import LOGS_DIR

os.makedirs(LOGS_DIR, exist_ok=True)
arquivo_log = os.path.join(LOGS_DIR, "smartwallet.log")

logging.basicConfig(
    filename=arquivo_log,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("smartwallet")